import codecs

import arrow
from slyguy import plugin, settings, inputstream
from slyguy.mem_cache import cached
from slyguy.session import Session

from .constants import M3U8_URL, REGIONS, EPG_URL
from .language import _

@plugin.route('')
def home(**kwargs):
    folder = plugin.Folder(cacheToDisc=False)

    folder.add_item(label=_(_.LIVE_TV, _bold=True), path=plugin.url_for(live_tv))

    if settings.getBool('bookmarks', True):
        folder.add_item(label=_(_.BOOKMARKS, _bold=True), path=plugin.url_for(plugin.ROUTE_BOOKMARKS), bookmark=False)

    folder.add_item(label=_.SETTINGS, path=plugin.url_for(plugin.ROUTE_SETTINGS), _kiosk=False, bookmark=False)

    return folder

@plugin.route()
def live_tv(**kwargs):
    region = get_region()
    channels = get_channels(region)

    folder = plugin.Folder(_(_.REGIONS[region]))

    if settings.getBool('show_epg', True):
        now = arrow.now()
        epg_count = 5
    else:
        epg_count = None

    for slug in sorted(channels, key=lambda k: (channels[k].get('network', 'zzzzzzz'), float(channels[k].get('channel', 'inf')), channels[k].get('name', 'zzzzzzz'))):
        channel = channels[slug]

        plot = u''
        count = 0
        if epg_count:
            if channel.get('epg_id') and not channel.get('programs'):
                channel['programs'] = channels.get(channel['epg_id'], {}).get('programs', [])

            for index, row in enumerate(channel.get('programs', [])):
                start = arrow.get(row[0])
                try: stop = arrow.get(channel['programs'][index+1][0])
                except: stop = start.shift(hours=1)

                if (now > start and now < stop) or start > now:
                    plot += u'[{}] {}\n'.format(start.to('local').format('h:mma'), row[1])
                    count += 1
                    if count == epg_count:
                        break

        if not count:
            plot += channel.get('description', '')

        folder.add_item(
            label = channel['name'],
            path = plugin.url_for(play, slug=slug, _is_live=True),
            info = {'plot': plot},
            art = {'thumb': channel.get('logo'), 'fanart': channel.get('fanart')},
            playable = True,
        )

    return folder

@plugin.route()
def play(slug, **kwargs):
    region = get_region()
    channel = get_channels(region)[slug]
    url = Session().head(channel['mjh_master'], allow_redirects=False).headers.get('location', '')

    item = plugin.Item(
        path = url or channel['mjh_master'],
        headers = channel.get('headers'),
        info = {'plot': channel.get('description')},
        art = {'thumb': channel.get('logo'), 'fanart': channel.get('fanart')},
        proxy_data = {'cert': channel.get('cert')},
    )

    if channel.get('hls', True):
        item.inputstream = inputstream.HLS(live=True)

    return item

@cached(60*5)
def get_channels(region):
    url = M3U8_URL.format(region=region)
    return Session().gz_json(url)

def get_region():
    return REGIONS[settings.getInt('region_index')]

@plugin.route()
@plugin.merge()
def playlist(output, **kwargs):
    region = get_region()
    channels = get_channels(region)

    with codecs.open(output, 'w', encoding='utf8') as f:
        f.write(u'#EXTM3U x-tvg-url="{}"'.format(EPG_URL.format(region=region)))

        for slug in sorted(channels, key=lambda k: (channels[k].get('network', ''), channels[k].get('name', ''))):
            channel = channels[slug]

            f.write(u'\n#EXTINF:-1 channel-id="{channel_id}" tvg-id="{epg_id}" tvg-chno="{chno}" tvg-logo="{logo}",{name}\n{url}'.format(
                channel_id=slug, epg_id=channel.get('epg_id', slug), logo=channel.get('logo', ''), name=channel['name'], chno=channel.get('chno', ''),
                    url=plugin.url_for(play, slug=slug, _is_live=True)))

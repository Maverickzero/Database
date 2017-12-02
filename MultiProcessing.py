import multiprocessing

StartPages = from_file('startPages.txt')
sites = list(set([urlparse(startpage).netloc.replace('www.','') for startpage in StartPages]))
resultsPerPage = 10
feeder_instances = [Feeder()] * len(sites)
# When setting useProxySpider in each instance of the getter to True a connection error uccors (because the start_proxyspider uses global variables), that's why it's started globally in this script.
#start_proxyspider()
def run_spider(i):
    startPages = [startpage for startpage in StartPages if sites[i] in startpage]
    feeder_instances[i].startPages = startPages
    feeder_instances[i].database_name = 'visited/%s_visited.db' % sites[i]
    feeder_instances[i].cookie_jar_type = 'mozilla'                                # memory or standard(native for cookiejar), mozilla (e.g. Netscape, curl format) or lwp (perl format)
    feeder_instances[i].cookiejar_filename = 'cookie.txt'                                 # Set the file where the cookies are stored. (Ignored if in memory mode)
    feeder_instances[i].cookiejar_save_exit = True                               # save changes to the cookiejar at the end of the run (ignored in archive)
    feeder_instances[i].country = 'nl'
    feeder_instances[i].subsiteName = sites[i] # 'ad.nl' # NOTE ad.nl subsiteName for all sites?

    # Getter specific options
    feeder_instances[i].commentOrder = 'asc'
    feeder_instances[i].articleFind = ['article//@href','*[@id="bcmostread"]//@href','*[contains(@class,"news")]/parent::a/@href', 'div[@class="topcenter"]//a/@href']

    feeder_instances[i].resultsPerPage = resultsPerPage

    try:
        baseUrl = baseUrlR.search(startPages[0]).group(1)
    except AttributeError:
        baseUrl = startPages[0]

    if feeder_instances[i].options.archive and sites[i] == 'https://www.arnhemsekoerier.nl/':
        feeder_instances[i].startPagesArchive = from_file('archivepages.txt')
    feeder_instances[i].cookies = [{"key":"nl_cookiewall_version","value":"1","domain":sites[i]}]
    feeder_instances[i].articleRegex = ['%s.+'%baseUrl,'^/.+'] # Previous version had sites[i] instead of baseUrl # NOTE this regex lead to wrong article urls
                                                               # ex wrong url: https://www.bndestem.nl/algemeen/bndestem.nl/algemeen/trump-zet-bizarre-traditie-voort%7Evaff7dc66/
    feeder_instances[i].crawl(getter=True)
    feeder_instances[i].urls_done = set()


# Starting the parallell processes on all cores minus one
pool = multiprocessing.Pool(processes=(multiprocessing.cpu_count()-1))
pool.map(run_spider, range(len(sites)))

pool.close()
pool.join()

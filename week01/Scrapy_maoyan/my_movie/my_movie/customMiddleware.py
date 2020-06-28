from fake_useragent import UserAgent
class CustomerUserAgent(object):
    def __init__(self,crawler):
        super(CustomerUserAgent,self).__init__()
        self.ua = UserAgent()
        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE','random')
    
    @classmethod
    def from_crawler(cls,crawler):
        return cls(crawler)

    def process_request(self,request,spider):
        def get_ua():
            return getattr(self.ua,self.ua_type)
        request.headers.setdefault('User_Agent',get_ua())
        request.headers.setdefault('Cookie','uuid_n_v=v1; uuid=1D84C250B84711EAACB6BBD781D8993834EE4332C14F43078A9812351CF1B4D3; mojo-uuid=5626779d6b188ad9cb357370abebe4a6; _lxsdk_cuid=172f4a90b2ac8-08c40deb6c77f7-f7d123e-144000-172f4a90b2ac8; _lxsdk=1D84C250B84711EAACB6BBD781D8993834EE4332C14F43078A9812351CF1B4D3; _csrf=ab509b8b2c599bd493ff3148994b5fe53475d33ee77fe3f17b87c1afeefe020f; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593272389,1593273208,1593349783,1593357316; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593359142; __mta=208974381.1593242618761.1593359037526.1593359142483.18; _lxsdk_s=172fbbb7c5b-eb0-78d-425%7C%7C1')
        # request.headers = {
        #     'Content-Type': 'text/plain; charset=UTF-8',
        #     'Origin': 'https://maoyan.com',
        #     'Referer': 'https://maoyan.com/films?showType=3',
        #     'User-Agent': get_ua(),
        #     'Cookie': 'uuid_n_v=v1; uuid=1D84C250B84711EAACB6BBD781D8993834EE4332C14F43078A9812351CF1B4D3; mojo-uuid=5626779d6b188ad9cb357370abebe4a6; _lxsdk_cuid=172f4a90b2ac8-08c40deb6c77f7-f7d123e-144000-172f4a90b2ac8; _lxsdk=1D84C250B84711EAACB6BBD781D8993834EE4332C14F43078A9812351CF1B4D3; _csrf=ab509b8b2c599bd493ff3148994b5fe53475d33ee77fe3f17b87c1afeefe020f; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593272389,1593273208,1593349783,1593357316; mojo-session-id={"id":"5e6578f5db976cb88c466fef17be80c4","time":1593364184436}; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593364184; __mta=208974381.1593242618761.1593361279698.1593364184809.20; mojo-trace-id=3; _lxsdk_s=172fbe7fda7-8ec-d16-e9%7C%7C3'}
        pass
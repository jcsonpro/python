import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BoardCrawlSpider(CrawlSpider):
    # 클로러의 이름
    name = 'board_crawl'

    # 크롤러 실행을 허용할 도메인 정의
    # 해당 서버에서 실행되다가 허용된 도메인 이외는 무시
    allowed_domains = ['kcomwel.or.kr']

    # 시작점으로 사용할 URL
    # 리스트로 지정 가능 - 여러 웹 페이지에서 크롤링을 시작하게 할 수 있다
    start_urls = [
        # https://www.kcomwel.or.kr/kcomwel/cust/pras/pras.jsp
        'https://www.kcomwel.or.kr/kcomwel/cust/pras/pras.jsp',
    ]


    # 크롤러가 어떻게 작동할지 규칙 설정
    # 크롤러는 시작점의 모든 링크를 검사한 후, 규칙에 맞는 링크가 있으면 정해진 콜백 메서드를 실행합니다
    # 규칙에 맞는 링크가 있으면 정해진 롤백 메서드를 실행
    # follow가 True면 해당 페이지의 링크를 대상으로 재귀적으로 앞 작업을 반복
    rules = (
        # Rule(
        #     # 크롤링할 링크를 정규 표현식을 이용해서 표현
        #     LinkExtractor(allow=r'Items/'), 
        #     # 해당 링크에 요청을 보내고 응답이 오면 실행할 콜백 메서드를 지정
        #     callback='parse_item', 
        #     # True로 설정되어 있으면, 응답에 다시 한번 rules를 적용해 재귀적으로 실행
        #     follow=True),

        # https://www.kcomwel.or.kr/kcomwel/cust/pras/pras.jsp?mode=view&article_no=1004313&board_wrapper=%2Fkcomwel%2Fcust%2Fpras%2Fpras.jsp&pager.offset=0&board_no=308
        # https://www.kcomwel.or.kr/kcomwel/cust/pras/pras.jsp?mode=view&article_no=1004288&board_wrapper=%2Fkcomwel%2Fcust%2Fpras%2Fpras.jsp&pager.offset=0&board_no=308
        Rule(LinkExtractor(allow=r'kcomwel/cust/pras/pras.jsp\?mode=view&article_no=.*&board_wrapper=%2Fkcomwel%2Fcust%2Fpras%2Fpras.jsp&pager.offset=0&board_no=308'), callback='parse_item', follow=True),
        # https://www.kcomwel.or.kr/kcomwel/cust/pras/pras.jsp?mode=list&board_no=308&pager.offset=10
        # https://www.kcomwel.or.kr/kcomwel/cust/pras/pras.jsp?mode=list&board_no=308&pager.offset=0
        # https://www.kcomwel.or.kr/kcomwel/cust/pras/pras.jsp?mode=list&board_no=308&pager.offset=20
        # https://www.kcomwel.or.kr/kcomwel/cust/pras/pras.jsp?mode=list&board_no=308&pager.offset=30
        Rule(LinkExtractor(allow=r'kcomwel/cust/pras/pras.jsp\?mode=list&board_no=308&pager.offset=\d0'))

    )
    
    def parse_item(self, response):
        # Rules를 통과한 링크에 요청을 보내 응답을 받으면 Rule()에 설정한 콜백 메서드를 해당 응답 결과에 실행
        """
            따라서, response를 파라미터로 받고 XPath라든가 CSS 선택자를 이용해서 원하는 요소를 추출
        """

        # 앞서 설정한 아이템에 맞춰 딕셔너리를 채우고 반환
        i = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        # //*[@id="sub"]/div[2]/table[1]/tbody/tr[1]/td[2]
        i['st_title'] = response.xpath(
                '//*[@id="is-cont"]/div[2]/div/div/div[7]/div[1]/table/tbody/tr[strong/text()=" 제목 : "]/td/text()').extract()
        
        i['st_content'] = response.xpath(
                '//*[@id="article_text"]/text()').extract()

        return i

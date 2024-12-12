from driver import Element
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import TimeoutException, NoSuchElementException

import time
class Crawl:
    url = "https://pedia.watcha.com/ko-KR/?domain=book"

        
    def __init__(self):
        self.element = Element()
        
        self.element.url(self.url)
        



    def kill(self):
        time.sleep(2)  # 잠시 대기
        self.element.quit()

   
    
    def set(self, keyword, year):
        
        self.element.url(self.url)
        self.year = year
        self.search_keyword = keyword


    def find_book(self):
        try:
            l = self.element.find_all(css_class = "bf517d4e5ad926d3a46d")

            for i in l:
                instance = i.find(css_class="b110f80385f63f81d7fe a0e21d46e180cf46b3ed")
                if instance.text() == "책":
                    return i.find_all(css_class = "c1fbb66dd0a8919a619b ef9348f4092a69aeb892")
        except Exception:
            return []


        

            


        
        return []
    
    def find_book_desc(self, url):
        desc_url = url + "/book_description"
        try:
            self.element.url(desc_url)
            t = self.element.find(css_class="d564474639d6d5b3ee56 f7d70d844d2e8db2758a ab3dccafc9ad33c8e788")
            if t.text().strip() !="":
                print("a")
                return t.text()
            try:
                self.element.url(url)
                tt = self.element.find(css_class="cbf385a8dfd716be802c")
                return tt.text().strip()
            except Exception as e:
                print("오류 발생 : ", e)
        except Exception as e:
            print("오류 발생:", e)

    def find(self):
        try:
            if len(self.element.find_all(css_class = "ce590159f8ac45244c5e a25d3170e302d030c207 WelcomeDisplayModal"))!=0:
                element_button = self.element.find(css_class = "de1b03570793cec2a50a")
                element_button.click()
                time.sleep(2)

        except Exception:
                print("팝업 없음")


        try:
            element_instance = self.element.find(css_class = "c8163d6897c44e00a656" )
            element_instance.click()
            input_field = self.element.find(id="desktop-search-field")
            input_field.send_keys(self.search_keyword)
            input_field.send_keys(Keys.RETURN)
            books = self.find_book()
            print(len(books))
            if len(books) == 0:
                return "no"
            if len(books) == 1:
                books[0].click()
                return self.find_book_desc(self.element.get_current_url())
            for book in books:
                field = book.find(css_class = "b0eed3ac8259acd0f04b cbf385a8dfd716be802c").text()[0:4]
                if field == self.year: 
                    book.click()
                    return self.find_book_desc(self.element.get_current_url())


            
        except Exception as e:
            print("오류발생:", e)
        finally:
            
            print()
        # 드라이버 종료
            



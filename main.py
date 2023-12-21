from enum import Enum
class Location(Enum):
    GradZagreb = 1153
    # TODO: add more locations

import requests
from bs4 import BeautifulSoup
class Njuskalo:
    def __init__(self, session=None):
        self.session = session or requests.Session()

    @staticmethod
    def as_logged_in(user, password):
        njuskalo = Njuskalo(session=requests.Session())
        response = njuskalo.iapi_get(
            "prijava/",
            headers={
                "Host": "iapi.njuskalo.hr",
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "DNT": "1",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Pragma": "no-cache",
                "Cache-Control": "no-cache",
            }
        )
        # TODO: add exception handling
        assert len(response.text) > 0
        soup = BeautifulSoup(response.text, "html.parser")
        token = soup.find("input", id="login__token")["value"]
        # TODO: add exception handling
        assert token
        data = f"login%5Busername%5D={user}&login%5Bpassword%5D={password}&login%5Bremember_me%5D=1&login%5BuseFacebookAccount%5D=&login%5BfbLoginActive%5D=&login%5B_token%5D={token}"
        response = njuskalo.iapi_post('prijava/',
            data=data,
            headers={
                "Host": "iapi.njuskalo.hr",
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Length": "256",
                "Origin": "https://iapi.njuskalo.hr",
                "DNT": "1",
                "Connection": "keep-alive",
                "Referer": "https://iapi.njuskalo.hr/prijava/",
                # TODO: "Cookie": "__uzma=dbb5656f-603b-43a7-8973-6924f66e1cab; __uzmb=1703142473; __uzme=3119; __uzmc=282541060337; __uzmd=1703142473; __uzmf=7f6000cb266744-9a04-4ff7-ac40-3128481085a617031424736990-8598f25bc30356ab10; njupop=cf103f3429f6ffd510434497d368c8f2130a292e42cfdfeeedeaadc0ba6e167a; PHPSESSID=b2b4457ce9c10d0984201d5b94ccff42; nuka-fp=085fa0df-b8b3-4f7d-9618-7be5ecc094ab; login_2fa=085fa0df-b8b3-4f7d-9618-7be5ecc094ab",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Pragma": "no-cache",
                "Cache-Control": "no-cache",
            }
        )
        return njuskalo

    def iapi_get(self, args, headers=None):
        headers = headers or {
            "Host": "iapi.njuskalo.hr",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
            # TODO: "Cookie": "__uzma=dbb5656f-603b-43a7-8973-6924f66e1cab; __uzmb=1703142473; __uzme=3119; __uzmc=322881648236; __uzmd=1703142700; __uzmf=7f6000cb266744-9a04-4ff7-ac40-3128481085a61703142473699227010-9e6b540e53653bc716; njupop=149daa1e0305fe1903a729e056e7e7b40a3430dc56e323fffb2088ca5edcf4e6; PHPSESSID=44992a31c87e9352dee24c51915a5d8f; nuka-fp=085fa0df-b8b3-4f7d-9618-7be5ecc094ab; login_2fa=085fa0df-b8b3-4f7d-9618-7be5ecc094ab; REMEMBERME=Domain.UserBundle.Entity.Main.User%3Ac21va2U5%3A1705772498%3A8UmmiVKznw2HmReUQ7KgN_RSBb07nG8nxO7jXa6NBY4~Blw0-0h-YyGr6GCMV7w7hm_y9sL5lj6BFHQ7keAH3M8~; didomi_token=eyJ1c2VyX2lkIjoiMThjOGIzNzMtM2EyZC02MDVlLTg0ZmYtOTA1NzNjNGM5NmU1IiwiY3JlYXRlZCI6IjIwMjMtMTItMjFUMDc6MTE6NDAuMDc3WiIsInVwZGF0ZWQiOiIyMDIzLTEyLTIxVDA3OjExOjQwLjA3N1oiLCJ2ZXJzaW9uIjpudWxsfQ==; njuskalo_adblock_detected=false",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "TE": "trailers",
        }
        url = "https://iapi.njuskalo.hr/" + args
        response = self.session.get(url, headers=headers, timeout=20)
        response.raise_for_status()
        return response

    def iapi_post(self, args, data, headers):
        url = "https://iapi.njuskalo.hr/" + args
        response = self.session.post(url, data=data, headers=headers, timeout=20)
        response.raise_for_status()
        return response

    def get_categories(self):
        resp = self.iapi_get("sitemap")
        assert len(resp.text) > 0
        soup = BeautifulSoup(resp.text, "html.parser")
        pssg_std_uls = soup.find("div", class_="passage-standard").find_all("ul", recursive=False)
        assert len(pssg_std_uls) == 2
        return [a["href"].replace("https://www.njuskalo.hr/", "") for a in pssg_std_uls[1].find_all("a")]

    def get_items(self, category, page=1, location=None):
        page = f"&page={page}"
        location = f"&locationId={location.value}" if location else ""
        args = f"{category}/?{page}{location}"

        response = self.iapi_get(args)
        # TODO: add exception handling
        assert len(response.text) > 0
        soup = BeautifulSoup(response.text, 'html.parser')
        scraped = soup.find_all("li", class_="EntityList-item--Regular")
        filtered = filter(lambda i: i.find("span", class_="icon-item feature feature--User") != None, scraped)
        items = []
        for f in filtered:
            href = f.find("a", class_="link")["href"]
            # TODO: add Item class
            items.append({
                "title": f.find("h3", class_="entity-title").get_text(),
                "link": f"""https://www.njuskalo.hr{href}""",
                "id": f.find("a", class_="link")["name"],
                "location": f.find("div", class_="entity-description-main").get_text().strip().replace("Lokacija: ", ""),
                "pubdate": f.find("time", class_="date date--full")["datetime"],
                "price": float(f.find('strong', class_="price").text.strip().split()[0].strip().replace('.', '').replace(',', '.')),
                "category": href.split("/")[1],
            })
        return items

def get_all_items(njuskalo, category, location=None):
    items = []
    page = 1
    while True:
        try:
            new_items = njuskalo.get_items(category, page, location)
        except requests.exceptions.HTTPError as e:
            # TODO: break only on 404 error, else raise
            break
        if len(new_items) == 0:
            break
        items += new_items
        page += 1
    return items

def main():
    import os
    user = os.getenv('NUSER')
    password = os.getenv('NPASS')

    print("Scraping all of njuskalo.hr...")

    if None in (user, password):
        print("Accessing as guest...")
        njuskalo = Njuskalo()
    else:
        print("Logging in...")
        njuskalo = Njuskalo.as_logged_in(user, password)

    print("Getting categories...")
    ctgs = njuskalo.get_categories()
    print("Getting items...")
    import concurrent.futures
    with concurrent.futures.ProcessPoolExecutor() as executor:
        args = [(njuskalo, ctg, Location.GradZagreb) for ctg in ctgs]
        for ctg,items in zip(ctgs, executor.map(get_all_items, *zip(*args))):
            print(f"{ctg}: {len(items)}")

    print("Done.")

if __name__ == "__main__":
    main()

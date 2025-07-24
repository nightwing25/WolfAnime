#https://youtu.be/u3Ue6IlzbOE?si=7PqBXSsoTmJLIBXx help for changing screens
#https://youtu.be/6uGZfBTl8Xc?si=em9MfFfAQ0RV1_E6 userinput
#https://youtu.be/oc09fkWZVOQ?si=9u8IOrK_0jahyt9P  adding widget dynamically
#https://stackoverflow.com/questions/70041675/how-can-get-input-from-mdtextfield-when-i-press-enter 
import os
#from plyer import call
import requests
from kivy.metrics import dp
from bs4 import BeautifulSoup as bs
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivy.network.urlrequest import UrlRequest
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from urllib.parse import quote
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty,ColorProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import Image
from threading import Thread
from kivy.clock import Clock
from kivymd.uix.navigationdrawer import (
    MDNavigationDrawer,MDNavigationDrawerItem, MDNavigationDrawerItemTrailingText
)
from kivymd.uix.button import MDIconButton
from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivymd.uix.textfield import (
    MDTextField,
    MDTextFieldLeadingIcon,
    MDTextFieldHintText,
    MDTextFieldHelperText,
    MDTextFieldTrailingIcon,
    MDTextFieldMaxLengthText,
    )
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.list import (
        MDListItem,
        MDListItemHeadlineText,
        MDListItemSupportingText,
        MDListItemTertiaryText,
        )
from kivymd.uix.imagelist import (
    MDSmartTile,
    MDSmartTileImage,
    MDSmartTileOverlayContainer,
)
from jnius import autoclass, cast
from android import activity, mActivity
os.environ['KIVY_WINDOW'] = 'sdl2'
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from pygame import mixer
from pygame import mixer

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load('(FREE) LO-FI TYPE BEAT - ＂ONE LOVE＂ [tVcwohev7Aw].ogg')

# Setting the volume
mixer.music.set_volume(0.1)

# Start playing the song
mixer.music.play()

# infinite loop
#while True:
#
#    print("Press 'p' to pause, 'r' to resume")
#    print("Press 'e' to exit the program")
#    query = input("  ")
#
#    if query == 'p':
#
#        # Pausing the music
#        mixer.music.pause()
#    elif query == 'r':
#
#        # Resuming the music
#        mixer.music.unpause()
#    elif query == 'e':
#
#        # Stop the mixer
#        mixer.music.stop()
#        break
#DO THE ONELINELISTITEM IN NAV DRAWER SETUP
#CREATE VIDEO AREA AFTER THE EITHER CARD IS PICKED 
#THEN UNDER VIDEO DISPLAY EPISODES AND SEASONS CLICK EPISODE ADD TO VIDEO TO BE VIEWED
#NEED COMPUTER(MAYBE) TO GET THE VIDEO URL 
#IF THERES EPISODES OR SEASON I WANT TO DISPLAY THEM ON ANOTHER SCREEN
#from kivy.clock import Clock
#play low lofi music playlist 
#last viewed history
#add a now playing feature for the music 
#create a watch together feature may need socket programming 

#for getting anime may need to encode the name and built in capitalize funct

#nav drawer empty asl 

KV = """


<ResponsiveGrid@GridLayout>:
    min_card_width: 300
    size_hint_y: None
    height: self.minimum_height
    spacing: "20dp"
    padding: "20dp"

<Naver>
    id: naver_root # if needed in python 
    #md_bg_color: self.theme_cls.backgroundColor
    MDTopAppBar:
        type: "small"  # or "center-aligned", "medium", etc.
        pos_hint: {"top": 1}

        MDTopAppBarLeadingButtonContainer:
            MDActionTopAppBarButton:
                icon: "menu"
                on_release: app.root.ids.nav_drawer.set_state("toggle")
        MDTopAppBarTitle:
            text:"WOLFANIME"
            halign:"center"




MainLayout:
    id:nav_layout
    ScreenManager:
        id:screen_manager
        UrlSearch:
            name:"SearchPage"
        Anime_Display_Page:
            name:"main_page"
        Episode_Season_Screen:
            name:"seasonEP"
        Socials:
            name:"socials_page"
        Manga:
            name:"manga_page"
        Setz:
            name:"settings_page"

    MDNavigationDrawer:
        id: nav_drawer
        radius: 0, dp(16), dp(16), 0

        MDNavigationDrawerMenu:
            MDNavigationDrawerHeader:
                title:"Menu"
                text:"header text"
                spacing: "4dp"
                padding: "12dp", 0, 0, "56dp"

            MDNavigationDrawerLabel:    
                text: "Menu"


            MDNavigationDrawerItem:
                on_release:
                    nav_drawer.set_state("close")
                    app.root.ids.screen_manager.current = "SearchPage"

                MDNavigationDrawerItemLeadingIcon:
                    icon:"magnify"
                MDNavigationDrawerItemText:
                    text:"Search"
            MDNavigationDrawerDivider:

            MDNavigationDrawerItem:
                on_release:
                    nav_drawer.set_state("close")
                    app.root.ids.screen_manager.current = "main_page"

                MDNavigationDrawerItemLeadingIcon:
                    icon: "face-man-shimmer"
                MDNavigationDrawerItemText:
                    text:"Anime"

            MDNavigationDrawerDivider:


            MDNavigationDrawerItem:
                on_release:
                    nav_drawer.set_state("close")
                    app.root.ids.screen_manager.current = "socials_page"

                MDNavigationDrawerItemLeadingIcon:
                    icon: "instagram"
                MDNavigationDrawerItemText:
                    text:"Socials"

            MDNavigationDrawerDivider:

            MDNavigationDrawerItem:
                on_release:
                    nav_drawer.set_state("close")
                    app.root.ids.screen_manager.current = "manga_page"

                MDNavigationDrawerItemLeadingIcon:
                    icon: "book-heart-outline"
                MDNavigationDrawerItemText:
                    text:"Manga"

            MDNavigationDrawerDivider:

            MDNavigationDrawerItem:
                on_release:
                    nav_drawer.set_state("close")
                    app.root.ids.screen_manager.current = "settings_page"


                MDNavigationDrawerItemLeadingIcon:
                    icon: "cog"
                MDNavigationDrawerItemText:
                    text:"Settings"


<Setz>:
    #set up manga part just like MySmartTile 
    FitImage:
        source:"bg.jpg"
        canvas.before:
            Color:
                rgba: 0, 0, 0, 0.5
            Rectangle:
                pos: self.pos
                size: self.size
        

    Naver:
    MDLabel:
        text:"settings page"
        halign:"center"


<Socials>:
    #put music section in socials 
    #add insta,x,github,soundcloud & youtube

    FitImage:
        source:"bg.jpg"
        canvas.before:
            Color:
                rgba: 0, 0, 0, 0.5
            Rectangle:
                pos: self.pos
                size: self.size
        

    Naver:
    MDBoxLayout:
        adaptive_size:True
        pos_hint: {'center_x':0.5,'center_y':0.5}
        orientation:"vertical"
        MDIconButton:
            icon:"instagram"
        MDIconButton:
            icon:"twitter"
        MDIconButton:
            icon:"soundcloud"
        MDIconButton:
            icon:"youtube"
            

<Manga>:
    #set up manga part just like MySmartTile 
    FitImage:
        source:"bg.jpg"
        canvas.before:
            Color:
                rgba: 0, 0, 0, 0.5
            Rectangle:
                pos: self.pos
                size: self.size
        

    Naver:
    MDLabel:
        text:"manga page"
        halign:"center"


<MySmartTile>:
    #pos_hint:{"center_x":.5,"center_y":.5}
    #size_hint:None,None
    #size:"175dp","175dp"
    #overlap:True

    #MDSmartTileImage:
    #    source:root.image_source
    #    radius:[dp(24),dp(24),0,0]

    #MDSmartTileOverlayContainer:
    #    md_bg_color:0,0,0,.5
    #    adaptive_height:True
    #    padding:"8dp"
    #    spacing:"8dp"
    #    radius:[0,0,dp(24),dp(24)]

    #    MDLabel:
    #        text:root.text
    #        theme_text_color:"Custom"
    #        text_color:"white"
    #        role:"small"
    

    

<MyCard>:
    elevation:40
    size_hint_y:None
    height:"250dp"

    MDBoxLayout:
        orientation: "vertical"
        padding:"5dp"
        AsyncImage:
            source:root.image_source
            size_hint: (1,1)
        MDLabel:
            text:root.text
            size_hint:(1,.60)
            halign:"center"
            #theme_text_color:'Custom'
            text_color:[1,1,1,1]



<UrlSearch>:
    id:UrlPage
    FitImage:
        source:"bg.jpg"
    Naver:
    MDTextField:
        id:search
        mode: "outlined"
        size_hint_x: None
        width: "240dp"
        pos_hint: {"center_x": .5, "center_y": .5}
        
        on_text_validate:if len(self.text) > 3: app.on_enter(self)

       # MDTextFieldLeadingIcon:
       #     icon: "account"

        MDTextFieldHintText:
            text: "search anime"

        MDTextFieldHelperText:
            text: "search anime by name"
            mode: "persistent"

        MDTextFieldTrailingIcon:
            icon: "magnify"

<Episode_Season_Screen>:
    FitImage:
        source:"bg.jpg"
    MDLabel:
        text:"hello world"
        halign:"center"
    Naver:
    ScrollView:
        pos_hint:{"top":.9}
        ResponsiveGrid:
            cols:4
            id:widget_box
            size_hint_y:None
            height:self.minimum_height
            padding:"20dp"
            spacing:"20dp"


<Anime_Display_Page>:
    id: main
    FitImage:
        source:"bg.jpg"
    Naver:
    ScrollView:
        pos_hint:{"top":.9}
        ResponsiveGrid:
            cols:4
            id:result_box
            size_hint_y:None
            height:self.minimum_height
            padding:"20dp"
            spacing:"20dp"

"""


#make class for search 
#make class for layout for searched results
#create bottom nav bar
class MainLayout(MDNavigationLayout):
    pass

class Naver(MDBoxLayout):
    pass

class UrlSearch(Screen):
    pass

class EpSeason(Screen):#video
    pass

class OtherSearch(MDBoxLayout):
    pass

class Anime_Display_Page(Screen): #layout for searched results 
    pass


class ResponsiveGrid(GridLayout):
    min_card_width = NumericProperty(180)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(size=self._adjust_cols)
        Clock.schedule_once(lambda dt: self._adjust_cols())  # Initial setup

    def _adjust_cols(self, *args):
        self.cols = max(1, int(Window.width / self.min_card_width))

class Setz(Screen):
    pass

class Socials(Screen):
    pass

class Manga(Screen):
    pass

class Episode_Season_Screen(Screen):
    pass

class Ep_season_list(MDListItem):
    images = StringProperty()
    episode = StringProperty()
    season = StringProperty()




class MySmartTile(MDSmartTile,ButtonBehavior):
    text = StringProperty()
    image_source = StringProperty()
    url = StringProperty()

    def on_press(self):
        print("hello world")
        app = MDApp.get_running_app()
        app.show_season_ep()
        #give the same functions as card 
        #from threading import Thread 
        #Thread(target=self.get_and_open_stream_url,daemon=True).start()

class MyCard(MDCard,ButtonBehavior):
    '''Implements a material card.'''
    text = StringProperty()
    image_source = StringProperty()
    url = StringProperty()
    #season = StringProperty()
    #episode = StringProperty()
    #set up mycard look in kv file
    
    def on_press(self):
        from threading import Thread 
        Thread(target=self.get_and_open_stream_url,daemon=True).start()


    def get_and_open_stream_url(self):
        try:
            headers = {
                    "User-Agent":"Mozilla/5.0",
                    "Referer":"https://hianime.to",
                    }
            resp = requests.get(self.url,headers=headers)
            if resp.status_code != 200:
                print("[!] Failed to fetch anime page")
                return
            soup = bs(resp.text,"html.parser")

            ep_tag = soup.select_one("a.ep-item")
            if not ep_tag:
                print("[!] No episodes found")
                return
            ep_url = "https://hianime.to" + ep_tag.get("href")

            ep_resp = requests.get(ep_url,headers=headers)
            if ep_resp.status_code != 200:
                print("[!] Failed to load episode")
                return

            match = re.search(r'https?://[^\'"]+\.m3u8',ep_resp.text)
            if not match:
                print("[!] couldnt find .m3u8 stream url")
                return

            stream_url = match.group(0)
            print("[*] Found stream:",stream_url)

            app = MDApp.get_running_app()
            app.open_in_browser(stream_url)
        except Exception as e:
            print("[!] Error in get_and _open_stream_url:",e)


    def get_and_play_first_episode(self):
        try:
            headers={
                    "User-Agent":"Mozilla/5.0",
                    "Referer":"https://hianime.to",
                    }
            resp = requests.get(self.url,headers=headers)
            if resp.status_code != 200:
                print("[!] Failed to fetch anime page.")
                return
            soup = bs(resp.text, "html.pasrer")

            ep_link_tag = soup.select_one("a.ep-item")
            if not ep_link_tag:
                print("[!] No episodes found.")
                return

            episode_href = ep_link_tag.get("href")
            if not episode_href:
                print("[!] Episode link not found")
                return

            episode_url = f"https://hianime.to{episode_href}"
            print("[*] Launching:",episode_url)

            #from subprocess import Popen
            #Popen(["mpv",episode_url])
            open_in_default_player(episode_url)
        except Exception as e:
            print("[!] Error in get_and_paly_first_episode", e)



class ManiApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Pink"
        return Builder.load_string(KV)


    def fetch_anime(self, search_query):
        from urllib.parse import quote
        url = f"https://hianime.to/search?keyword={quote(search_query)}"
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Referer': url,
        }

        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                Clock.schedule_once(lambda dt: self.on_html_success(response.text))
            else:
                print(f"[!] Failed with status code {response.status_code}")
        except Exception as e:
            print(f"[!] Request error: {e}")

    
    def on_enter(self,instance):
        search_query = instance.text
        Thread(target=self.fetch_anime,args=(search_query,),daemon=True).start()



    def open_in_browser(self,url):
        Intent = autoclass('android.content.Intent')
        Uri = autoclass('android.net.Uri')

        intent = Intent(Intent.ACTION_VIEW)
        intent.setData(Uri.parse(url))
        mActivity.startActivity(intent)


    def open_in_default_player(self,url):
        Intent = autoclass('android.content.Intent')
        Uri = autoclass('android.net.Uri')

        intent = Intent(Intent.ACTION_VIEW)
        intent.setData(Uri.parse(url))
        chooser = Intent.createChooser(intent, "Open with")
        mActivity.startActivity(chooser)




   # def play_episode_in_mpv(episode_page_url):#ai exammple
   #     headers = {
   #         "User-Agent": "Mozilla/5.0",
   #         "Referer": "https://hianime.to/",
   #     }
   #     resp = requests.get(episode_page_url, headers=headers)
   #     if resp.status_code != 200:
   #         print("[!] Page request failed:", resp.status_code)
   #         return

   #     html = resp.text

   #     # 1️⃣ Try direct .m3u8 find
   #     m = re.search(r'https?://[^"\']+\.m3u8', html)
   #     if m:
   #         stream_url = m.group(0)
   #     else:
   #         # 2️⃣ If it's inside JSON or JS variable like `sources:[{file:"URL"}]`
   #         m = re.search(r'file\s*:\s*"([^"]+\.m3u8)"', html)
   #         if m:
   #             stream_url = m.group(1)
   #         else:
   #             print("[!] Could not find .m3u8 link in page.")
   #             return

   #     print("[*] Stream URL:", stream_url)
   #     os.system(f'mpv "{stream_url}"')


    def on_html_success(self, html_text):
        soup = bs(html_text, "html.parser")
        items = soup.find_all("div", class_="flw-item")

        screen_manager = self.root.ids.screen_manager
        main_page = screen_manager.get_screen("main_page")
        result_box = main_page.ids.result_box
        result_box.clear_widgets()

        for item in items:
            poster_div = item.find("div", class_="film-poster")
            img = poster_div.find("img", class_="film-poster-img")
            a_tag = poster_div.find("a",href=True)
            if not img or not a_tag:
                continue
            #if not img and f'{search_query}' not in img and poster_div:
             #   continue

            image_url = img.get("data-src") or img.get("src")
            title = img.get("alt") or "Untitled"
            anime_url = "https://hianime.to" +a_tag['href']

            #if not image_url or not image_url.startswith("http"):
             #   continue

            #card = MyCard(text=title, image_source=image_url,url=anime_url)
            #result_box.add_widget(card)
            tile = MySmartTile(
                MDSmartTileImage(
                    source=image_url,
                    radius=[dp(24), dp(24), 0, 0],
                ),

                MDSmartTileOverlayContainer(
                    MDLabel(
                        text=title,
                        theme_text_color="Custom",
                        text_color="white",
                        role='small'
                    ),
                    md_bg_color=(0, 0, 0, 0.5),
                    adaptive_height=True,
                    padding="12dp",
                    spacing="12dp",
                    radius=[0, 0, dp(24), dp(24)],
                ),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                size_hint=(None, None),
                size=("175dp", "175dp"),
                overlap=True,

            )
            result_box.add_widget(tile)

        screen_manager.current = "main_page"

    def show_season_ep(self):

        screen_manager = self.root.ids.screen_manager
        main_page = screen_manager.get_screen("main_page")

        screen_manager.current = "seasonEP"
   # def on_html_success(self, html_text):
   #     soup = bs(html_text, "html.parser")
   #     names = soup.find_all("a", class_="dynamic-name")
   #     for_imgs = soup.find_all('div',class_="tick ltr")
   #     #img_tags = soup.find_all("img", class_="film-poster-img")

   #     screen_manager = self.root.ids.screen_manager
   #     main_page = screen_manager.get_screen("main_page")
   #     result_box = main_page.ids.result_box
   #     result_box.clear_widgets()

   #     for i in range(min(len(names), len(img_tags))):
   #         title = names[i].get_text(strip=True)
   #         image_url = img_tags[i].get("data-src") or img_tags[i].get("src")

   #         if not image_url or not image_url.startswith("http"):
   #             continue
   #         #x = MDLabel(text=title)
   #         #b = MDLabel(text=image_url,allow_copy=True,adaptive_size=True,allow_selection=True,padding=("4dp","4dp")) #test code 
   #         card = MyCard(text=title, image_source=image_url)
   #         result_box.add_widget(card)
   #         #result_box.add_widget(b)

       # screen_manager.current = "main_page"


    def on_error(self, *args):
        print("failed to fetch url",args)


if __name__ == "__main__":
    ManiApp().run()

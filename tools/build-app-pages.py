#!/usr/bin/env python3
"""Builds the two app detail pages (daycount/index.html, musclememory/index.html) from the content below.

Why a script: every feature line exists in en + ko and every band repeats the same markup.
Edit the content here, run `python3 tools/build-app-pages.py`, review the diff, commit.

RULES
- Only list what is LIVE on the App Store. Check first:
    curl -s "https://itunes.apple.com/lookup?id=6834637942&country=kr"   # DayCount     -> 1.7 (2026-11-26)
    curl -s "https://itunes.apple.com/lookup?id=6834974384&country=kr"   # Muscle Memory -> 1.1 (2026-11-23)
- Work that is not on sale yet (e.g. Muscle Memory 1.2 chart) must NOT be added here. Keep drafts outside this repo
  (the 1.7 draft lived in day-count-deco/docs/site-next/) and move them into the lists when the version is READY_FOR_SALE.
- No location / residence wording. No emoji. See DESIGN.md.
"""
import html
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent


def T(en, ko):
    return f'<span lang="en">{html.escape(en, quote=False)}</span><span lang="ko">{html.escape(ko, quote=False)}</span>'


def img_pair(name, alt_en, alt_ko, folder="features", lazy=True, w=600, h=1253, prefix="../assets"):
    lz = ' loading="lazy" decoding="async"' if lazy else ""
    return (
        f'<img lang="en" src="{prefix}/{folder}/{name}-en.webp" width="{w}" height="{h}" alt="{html.escape(alt_en)}"{lz}>'
        f'<img lang="ko" src="{prefix}/{folder}/{name}-ko.webp" width="{w}" height="{h}" alt="{html.escape(alt_ko)}"{lz}>'
    )


# ---------------------------------------------------------------- content
# band = dict(id, title(en,ko), lead(en,ko), items[(en_head, ko_head, en_line, ko_line)], img=(name, alt_en, alt_ko, h) | None)

DAYCOUNT_BANDS = [
    dict(id="decorate", title=("Decorate your cards", "카드를 꾸며요"),
         lead=("Backgrounds, stickers, text and effects, on the card and on the widget.", "디데이 카드와 위젯을 내 마음대로 꾸며요."),
         img=("dc-deco-home", "DayCount list with decorated cards: a pink 100 days card, a Christmas D-30 card and a New Year party card", "분홍 100일째 카드, 크리스마스 D-30 카드, 연말 파티 카드 등 꾸민 카드가 보이는 데이카운트 목록", 1253),
         items=[
             ("Decorate", "꾸미기", "In Decorate on the detail screen, add backgrounds, stickers, text, drawings, effects and filters, then drag, pinch and rotate.", "상세 화면의 ‘꾸미기’에서 배경·스티커·글자·손그림·효과·필터를 얹고, 손가락으로 옮기고 키우고 돌려요."),
             ("On the widget too", "위젯에도 그대로", "A decorated D-Day shows the same design on your Home Screen widget, and the count stays up to date.", "꾸민 디데이는 홈 화면 위젯에도 같은 모습으로 나오고, 숫자는 오늘 기준으로 바뀌어요."),
             ("Your own stickers", "나만의 스티커", "Lift a person or object out of a photo to make a sticker. Photos are processed only on your device.", "사진에서 사람이나 물건만 오려 나만의 스티커로 만들어요. 사진은 기기 안에서만 처리돼요."),
             ("Undo, redo and drafts", "되돌리기와 임시 저장", "Step back and forward through your edits. Leave halfway and DayCount offers to pick up where you left off.", "편집을 한 단계씩 되돌리고 다시 해요. 중간에 나가도 이어서 할 수 있어요."),
         ]),
    dict(id="christmas", title=("Christmas stickers and effects", "크리스마스 스티커와 효과"),
         lead=("A Christmas pack for the season, ready in one tap.", "연말 분위기를 한 번에 입혀요."),
         img=("dc-deco-editor", "Decorate editor with a Christmas sticker, snow and a toolbar", "크리스마스 스티커와 눈 효과, 도구 막대가 있는 꾸미기 화면", 1253),
         items=[
             ("14 Christmas stickers", "크리스마스 스티커 14개", "A wreath, a tree, a candy cane, snowflakes, gifts and more.", "리스, 트리, 지팡이 사탕, 눈 결정, 선물 상자 등이 있어요."),
             ("Effects", "효과", "Snow, twinkling lights, confetti, hearts and fireworks. They keep moving in the app, in a GIF and in a video.", "눈·반짝이 전구·색종이·하트·불꽃 효과. 앱에서도, GIF와 영상에서도 계속 움직여요."),
             ("8 one-tap templates", "한 번에 입히는 템플릿 8개", "Start from a ready-made look and change anything you like.", "만들어 둔 모습으로 시작해서 마음에 드는 대로 바꿔요."),
             ("Milestone cards", "기념일 카드", "On day 100, anniversaries, D-30, the day itself and birthdays, a decorated share card is already prepared. Tap the reminder to open it.", "100일째·주년·D-30·D-Day·생일에는 꾸민 공유 카드가 미리 준비돼요. 알림을 누르면 바로 열려요."),
         ]),
    dict(id="widgets", title=("Widgets and a tidy list", "위젯, 그리고 깔끔한 목록"),
         lead=("See every big day without opening the app.", "앱을 열지 않아도 중요한 날이 보여요."),
         img=("dc-home", "DayCount list with theme filters, favorites and D-Day counts", "테마 필터, 즐겨찾기, 디데이 목록이 보이는 데이카운트 홈 화면", 1253),
         items=[
             ("Three widget sizes", "위젯 3가지 크기", "Small, medium and large show 1, 4 or 6 D-Days.", "소형·중형·대형에 디데이를 1개, 4개, 6개까지 보여 줘요."),
             ("Choose what each widget shows", "위젯마다 보여 줄 디데이 고르기", "Touch and hold a widget, tap Edit Widget, and pick its D-Days.", "위젯을 길게 눌러 위젯 편집에서 디데이를 골라요."),
             ("Sort your way", "정렬은 내 마음대로", "Favorites first, nearest date, recently added, or drag into your own order. Widgets follow it.", "즐겨찾기 우선, 가까운 순, 최근 등록 순, 직접 정한 순. 위젯도 같은 순서를 따라요."),
             ("Favorites and themes", "즐겨찾기와 테마 필터", "Star the ones that matter and filter the list by theme.", "중요한 디데이에 별을 달고, 테마별로 모아 봐요."),
             ("Pull to refresh", "당겨서 새로고침", "Pull the list down to recount from today.", "목록을 아래로 당기면 오늘 기준으로 다시 계산해요."),
         ]),
    dict(id="add", title=("Add a D-Day in seconds", "몇 초 만에 디데이 등록"),
         lead=("Pick a theme, type a title, choose the date.", "테마를 고르고, 제목을 쓰고, 날짜만 고르세요."),
         img=("dc-composer", "New D-Day screen with theme chips, a date wheel and repeat options", "테마 칩, 날짜 휠, 반복 옵션이 있는 새 디데이 화면", 1253),
         items=[
             ("Quick templates", "빠른 템플릿", "Anniversary, exam, trip, birthday, wedding, due date, diet, 100 days and more.", "기념일·시험·여행·생일·결혼·출산 예정일·다이어트·100일·전역 등."),
             ("Count down or count up", "남은 날과 지난 날", "D- for what is ahead, D+ for the days since.", "남은 날(D-)과 지난 날(D+)을 모두 세요."),
             ("Start date as Day 1", "시작일을 1일로", "Turn it on for a D-Day to count the first day as Day 1, the way “100 days” is counted.", "만난 날을 1일로 세는 방식을 디데이마다 켜고 끌 수 있어요."),
             ("Repeats, age and anniversaries", "반복, 만 나이, 주년", "Repeat yearly, monthly or weekly. Birthdays show age, anniversaries show the year count.", "매년·매월·매주 반복. 생일은 만 나이, 기념일은 주년을 보여 줘요."),
             ("Lunar dates", "음력 날짜", "Lunar birthdays are recalculated every year.", "음력 생일도 매년 알아서 계산해요."),
             ("Duplicate check", "중복 확인", "Saving a D-Day you already have? DayCount asks first.", "같은 디데이를 또 저장하려고 하면 먼저 알려 드려요."),
         ]),
    dict(id="reminders", title=("Reminders you set", "알림은 내가 정해요"),
         lead=("Choose the days and the time, for each D-Day.", "디데이마다 날짜와 시간을 골라요."),
         img=None,
         items=[
             ("Pick the days", "알림 날짜", "30, 7, 3 or 1 day before, or the day itself. Any mix.", "30일·7일·3일·1일 전과 당일 중 원하는 만큼 골라요."),
             ("Pick the time", "알림 시간", "Every D-Day has its own reminder time.", "디데이마다 시간을 따로 정해요."),
             ("Time Sensitive for birthdays and anniversaries", "기념일은 시간 민감 알림", "Reminders for the day before and the day itself can get through Focus. Turn this off in Settings.", "생일·기념일의 D-1·당일 알림은 집중 모드에서도 놓치지 않아요. 설정에서 끌 수 있어요."),
             ("To-dos in the reminder", "할 일 개수도 함께", "A reminder tells you how many to-dos are left for that year.", "알림에 그해 남은 할 일 개수도 같이 알려 드려요."),
         ]),
    dict(id="year", title=("A record for every year", "해마다 남기는 기록"),
         lead=("Birthdays and anniversaries come back every year. Your notes can too.", "해마다 돌아오는 날, 그해의 메모도 남겨 두세요."),
         img=("dc-detail", "D-Day detail screen with age, which birthday it is, and Edit and Delete buttons", "만 나이와 몇 번째 생일인지, 수정·삭제 버튼이 보이는 디데이 상세 화면", 1253),
         items=[
             ("Notes and to-dos", "메모와 할 일", "Write a note and a checklist for each year of a D-Day.", "디데이마다 그해의 메모와 할 일을 적어요."),
             ("Copy last year's to-dos", "작년 할 일 가져오기", "Bring them in with one tap and check them off again.", "한 번에 가져와 올해 다시 체크해요."),
             ("Look back", "지난해 다시 보기", "This year stays open. Tap a past year to see it.", "올해는 펼쳐져 있고, 지난해는 눌러서 볼 수 있어요."),
             ("Age and which birthday", "나이와 몇 번째", "The detail screen shows the age and which birthday, or which anniversary, it is.", "상세 화면에 만 나이와 몇 번째 생일(또는 주년)인지 나와요."),
             ("Only on your iPhone", "내 아이폰에만", "Notes are never put into shared cards or links.", "기록은 공유 카드나 링크에 들어가지 않아요."),
         ]),
    dict(id="share", title=("Share a D-Day", "디데이 나누기"),
         lead=("Send it as an image, a GIF, a video or a link.", "이미지, GIF, 영상, 링크로 보내 보세요."),
         img=None,
         items=[
             ("Image, GIF or video", "이미지, GIF, 영상", "Save a card that looks like your widget, decorated or plain, as an image, an animated GIF or a video, in square or story size.", "위젯 모양 카드를 꾸민 그대로 이미지, 움직이는 GIF, 영상으로 저장해요. 정사각형과 스토리 크기가 있어요."),
             ("Instagram Stories", "인스타그램 스토리", "Send a story-size card straight to Instagram Stories. Use the share sheet for Messages, KakaoTalk and more.", "스토리 크기 카드를 인스타그램 스토리로 바로 보내요. 카카오톡·메시지 등은 공유 시트로 보내요."),
             ("Send as a link", "링크로 보내기", "Your friend taps it and adds the D-Day in one step. Only the title and date are in the link, and nothing is stored anywhere.", "받은 사람이 링크를 누르면 바로 추가돼요. 제목과 날짜만 담기고, 어디에도 저장되지 않아요."),
             ("Send a design", "디자인 링크", "Share a decoration as a link. Your friend opens it in DayCount and taps Use this design. Your photos, titles and dates are left out.", "꾸민 디자인을 링크로 보내요. 받은 사람이 데이카운트에서 열고 ‘이 디자인 쓰기’를 누르면 적용돼요. 내 사진, 제목, 날짜는 빠져요."),
             ("Celebrations", "기념일 축하", "On Day 100, anniversaries and the day itself, petals fall and you can send a card right away.", "100일째, N주년, 디데이 당일에는 꽃잎과 축하 문구가 나와요. 바로 카드로 보낼 수 있어요."),
             ("A new day", "하루가 지나면", "Open the app on a new day and the count rolls over from yesterday to today.", "앱을 열면 남은 날이 어제에서 오늘로 넘어가는 모습을 보여 줘요."),
         ]),
    dict(id="calendar", title=("Add to your Calendar", "캘린더에 추가"),
         lead=("One tap from the detail screen.", "상세 화면에서 한 번에."),
         img=None,
         items=[
             ("Add to Calendar", "아이폰 캘린더에 추가", "Tap the calendar button at the top of the detail screen to get an all-day event, ready to save.", "상세 화면 위쪽의 캘린더 버튼을 누르면 하루 종일 일정으로 채워져요."),
             ("Repeats and a reminder", "반복과 하루 전 알림", "Yearly, monthly or weekly repeats and a reminder the day before come along. Lunar D-Days are added once, on the next date.", "매년·매월·매주 반복과 하루 전 알림까지 함께 들어가요. 음력 디데이는 다가오는 날짜로 한 번 추가돼요."),
         ]),
    dict(id="style", title=("Make it yours", "내 취향대로"),
         lead=("Colors, emoji, and an app icon with a face.", "색, 이모지, 그리고 표정이 바뀌는 앱 아이콘."),
         img=("dc-icon", "Four DayCount app icon faces that change as a D-Day gets closer", "디데이가 다가오면 바뀌는 데이카운트 앱 아이콘 표정 4가지", 1253),
         items=[
             ("An app icon with a face", "표정이 바뀌는 앱 아이콘", "The face changes as your next D-Day gets closer. Choose from 6 colors, or turn it off.", "디데이가 다가오면 표정이 바뀌어요. 6가지 색 중에 고르고, 끌 수도 있어요."),
             ("28 colors, or any color", "28가지 색, 또는 직접", "Your list and widget follow the color you choose.", "고른 색으로 목록과 위젯이 바뀌어요. 원하는 색을 직접 골라도 돼요."),
             ("Emoji icons", "이모지 아이콘", "Use any iPhone emoji as a D-Day's icon.", "디데이마다 원하는 이모지를 아이콘으로 써요."),
             ("9 appearances", "화면 모드 9가지", "System, Light and Dark, plus Cream, Blush, Sage, Sky, Midnight and Black.", "시스템·라이트·다크에 크림·블러시·세이지·스카이·미드나잇·블랙."),
             ("The DayCount character", "홈 화면 캐릭터", "The character on the Home screen changes its face with your next D-Day.", "홈 화면의 캐릭터가 다가오는 디데이에 따라 표정을 바꿔요."),
             ("8 languages", "8개 언어", "Korean, English, Japanese, Traditional Chinese, German, Spanish, French and Portuguese. Change it in Settings and widgets and reminders follow.", "한국어·영어·일본어·중국어(번체)·독일어·스페인어·프랑스어·포르투갈어. 설정에서 바꾸면 위젯과 알림도 바로 바뀌어요."),
         ]),
    dict(id="backup", title=("Backup and privacy", "백업, 그리고 개인정보"),
         lead=("Your D-Days stay on your iPhone. The backup file is yours to keep.", "디데이는 내 아이폰에만 있어요. 백업 파일은 직접 보관해요."),
         img=None,
         items=[
             ("Backup file", "백업 파일", "Create one in Settings, save it to Files or send it to yourself. Open the file to restore.", "설정에서 만들어 파일 앱에 저장하거나 카카오톡 ‘나와의 채팅’·메일로 보내 두세요. 그 파일을 열면 바로 불러와요."),
             ("A nudge after 30 days", "30일이 지나면 알림", "If 30 days pass without a backup, DayCount reminds you gently in Settings and on the first screen.", "백업한 지 30일이 지나면 설정과 첫 화면에서 가볍게 알려 드려요."),
             ("Safe restore", "안전한 불러오기", "The file is checked first, and your current D-Days are kept as a snapshot before anything is replaced.", "파일을 먼저 확인하고, 바꾸기 전에 지금 디데이를 따로 보관해요."),
             ("Update notice", "새 버전 안내", "About once a day, DayCount reads its public version number from the App Store and shows a small notice when a new version is out. Nothing personal is sent, and offline nothing happens.", "하루에 한 번 정도 App Store의 공개 버전 번호를 확인해 새 버전이 나오면 작게 알려 드려요. 개인 정보는 보내지 않고, 인터넷이 없으면 아무 일도 없어요."),
             ("No account needed", "가입 없이 바로", "No sign-up, no tracking. Ads only play when you choose one to unlock a new decoration.", "로그인과 추적은 없어요. 광고는 새 꾸미기를 열 때 원하면 한 편만 봐요."),
         ]),
]

DAYCOUNT_FAQ = [
    ("How do I add the widget?", "위젯은 어떻게 붙이나요?",
     "Touch and hold an empty area of your Home Screen, tap Edit → Add Widget, search for DayCount, choose a size and tap Add Widget.",
     "홈 화면 빈 곳을 길게 누르고 편집 → 위젯 추가 → DayCount를 검색해 크기를 고른 뒤 위젯 추가를 누르세요."),
    ("Which D-Days does the widget show?", "위젯에는 어떤 디데이가 나오나요?",
     "By default, the same order as your list in the app, which follows the sort option you chose. To pick them yourself, touch and hold the widget, tap Edit Widget and choose the D-Days. Small shows 1, medium 4 and large 6.",
     "기본은 앱 목록과 같은 순서예요. 앱에서 고른 정렬을 따라가요. 직접 고르려면 위젯을 길게 눌러 위젯 편집에서 디데이를 고르세요. 소형은 1개, 중형은 4개, 대형은 6개까지 보여요."),
    ("The widget did not update.", "위젯이 바로 안 바뀌어요.",
     "Widgets refresh automatically at midnight and usually soon after you edit a D-Day. Pulling the list down in the app recounts from today and reloads them. Removing and re-adding the widget also forces a refresh.",
     "위젯은 자정마다, 그리고 디데이를 바꾼 뒤 보통 곧 새로고침돼요. 앱에서 목록을 아래로 당기면 오늘 기준으로 다시 계산하고 위젯도 다시 불러와요. 위젯을 지우고 다시 붙여도 바로 바뀌어요."),
    ("Is my data backed up?", "데이터가 백업되나요?",
     "D-Days are stored only on your iPhone and there is no cloud sync. In Settings you can create a backup file and save it to Files or send it to yourself. DayCount reminds you if 30 days pass without a backup. Without a backup file, deleting the app deletes your D-Days.",
     "디데이는 아이폰에만 저장되고 클라우드 동기화는 없어요. 설정에서 백업 파일을 만들어 파일 앱에 저장하거나 나에게 보내 둘 수 있어요. 백업한 지 30일이 지나면 알려 드려요. 백업 파일이 없으면 앱을 삭제할 때 디데이도 함께 지워져요."),
    ("How do I move my D-Days to a new iPhone?", "새 아이폰으로 옮기려면요?",
     "Create a backup file in Settings and send it to yourself. On the new iPhone, install DayCount, open the file and choose DayCount, or use the restore option in Settings. The backup holds your D-Days, yearly notes and to-dos, reminder settings and sort order. App language, appearance, icon color and which D-Days each widget shows are not included.",
     "설정에서 백업 파일을 만들어 나에게 보내 두세요. 새 아이폰에 데이카운트를 설치하고 그 파일을 열어 데이카운트를 고르거나, 설정의 불러오기를 쓰면 돼요. 디데이, 해마다 기록, 알림 설정, 정렬 순서가 담겨요. 앱 언어, 화면 모드, 아이콘 색, 위젯별 디데이 선택은 담기지 않아요."),
    ("How do I send a D-Day to a friend?", "친구에게 디데이를 보내려면요?",
     "Open the D-Day and tap Share. Send a card image, or a link. When your friend taps the link, DayCount asks whether to add it. The link holds only the title and date, and your notes are left out. If they do not have the app, the link opens a page with an App Store button.",
     "디데이 상세 화면에서 공유를 누르세요. 카드 이미지나 링크를 보낼 수 있어요. 받은 사람이 링크를 누르면 데이카운트에서 추가할지 물어봐요. 링크에는 제목과 날짜만 담기고 메모는 빠져요. 앱이 없으면 App Store 버튼이 있는 페이지가 열려요."),
    ("How do reminders work?", "알림은 어떻게 설정하나요?",
     "When you add or edit a D-Day, choose which days to be reminded (30, 7, 3 or 1 day before, or the day itself) and the time. You can turn reminders off in Settings. Count-up D-Days have no reminders. For Time Sensitive reminders to come through a Focus, also allow DayCount in the Focus settings of iOS.",
     "디데이를 등록하거나 고칠 때 알림 날짜(30일·7일·3일·1일 전, 당일)와 시간을 고르세요. 설정에서 알림을 끌 수 있어요. 지난 날(D+) 디데이에는 알림이 없어요. 시간 민감 알림이 집중 모드 중에도 오게 하려면 iOS 설정의 집중 모드에서 데이카운트를 허용해 두세요."),
    ("How do I add a lunar date?", "음력 날짜는 어떻게 넣나요?",
     "In the new D-Day screen, switch the date from Solar to Lunar. With yearly repeat on, the date is recalculated every year.",
     "새 디데이 화면에서 날짜를 양력에서 음력으로 바꾸세요. 매년 반복을 켜 두면 해마다 날짜를 다시 계산해요."),
    ("What does “Start date as Day 1” do?", "‘시작일을 1일로’는 뭔가요?",
     "For a D-Day in the past, turning it on counts the start date as Day 1 (shown as Day N), so “Day 100” lands 99 days after the start. Off, the start date is D+0 and you see D+N.",
     "지난 날 디데이에서 켜면 시작한 날을 1일로 세어 N일째로 보여 줘요. 그래서 100일째는 시작일 + 99일이에요. 끄면 시작일이 D+0이고 D+N으로 보여요."),
    ("How do I delete a D-Day?", "디데이는 어떻게 지우나요?",
     "Swipe the D-Day left in the list and tap Delete, then confirm. The confirmation shows which D-Day you are deleting.",
     "목록에서 디데이를 왼쪽으로 밀고 삭제를 누른 뒤 확인하세요. 확인창에 어떤 디데이인지 이름이 나와요."),
    (
        "How do I add a D-Day to my Calendar?", "캘린더에는 어떻게 추가하나요?",
        "Open the D-Day and tap the calendar button at the top. iOS shows a new event already filled in. You choose whether to save it. DayCount does not read your calendar.",
        "디데이 상세 화면 위쪽의 캘린더 버튼을 누르면 내용이 채워진 새 이벤트 화면이 열려요. 저장할지는 직접 정해요. 데이카운트는 캘린더를 읽지 않아요."),
    ("How do I decorate a D-Day?", "디데이는 어떻게 꾸미나요?",
     "Open the D-Day and tap Decorate at the bottom. Pick a background, add stickers, text, drawings, effects or a filter, then tap Save. The design also shows on the Home Screen widget. To start over, reset the decoration from the detail screen menu.",
     "디데이 상세 화면 아래쪽의 ‘꾸미기’를 누르세요. 배경을 고르고 스티커·글자·손그림·효과·필터를 얹은 뒤 저장을 누르면 돼요. 홈 화면 위젯에도 같은 디자인이 나와요. 처음으로 돌리려면 상세 화면 메뉴에서 꾸미기를 초기화하세요."),
    ("Are my photos uploaded?", "사진이 업로드되나요?",
     "No. Photos you use to decorate a D-Day stay on your iPhone and are processed on the device. Design links do not include your photos.",
     "아니요. 꾸미기에 쓴 사진은 아이폰에만 있고 기기 안에서 처리돼요. 디자인 링크에도 내 사진은 들어가지 않아요."),
    ("How do I save a card as a GIF or video, or send it to Instagram Stories?", "GIF·영상으로 저장하거나 인스타그램 스토리로 보내려면요?",
     "Open the D-Day and tap Share, then choose the format. Image, GIF and video can be saved to Photos or sent from the share sheet. Instagram Stories needs the Instagram app; without it, the normal share sheet opens.",
     "디데이 상세 화면에서 공유를 누르고 형식을 고르세요. 이미지·GIF·영상은 사진에 저장하거나 공유 시트로 보낼 수 있어요. 인스타그램 스토리는 인스타그램 앱이 있어야 하고, 없으면 일반 공유 시트가 열려요."),
    ("A friend sent me a design link.", "친구가 디자인 링크를 보냈어요.",
     "Tap the link. With DayCount installed it opens A friend's design, and nothing changes until you tap Use this design. Without the app, the link opens a page with an App Store button.",
     "링크를 누르면 데이카운트에 ‘친구가 보낸 디자인’이 열리고, ‘이 디자인 쓰기’를 누르기 전에는 아무것도 바뀌지 않아요. 앱이 없으면 App Store 버튼이 있는 페이지가 열려요."),
    ("What is the “new version available” notice?", "‘새 버전이 있어요’ 안내는 뭔가요?",
     "About once a day DayCount reads the public version number from the App Store and shows a small notice if a newer version exists. The request holds only the app's App Store ID and your region code. No personal data or D-Day contents are sent.",
     "하루에 한 번 정도 App Store의 공개 버전 번호를 읽어 새 버전이 있으면 작게 알려 드려요. 앱의 App Store 번호와 지역 코드만 보내고, 개인정보나 디데이 내용은 보내지 않아요."),
]

MUSCLEMEMORY_BANDS = [
    dict(id="next-weight", title=("Know what to lift next", "다음에 몇 kg 들지"),
         lead=("It reads your last session and tells you today's weight and reps.", "지난 기록을 보고 오늘 무게와 횟수를 알려줘요."),
         img=("mm-chart", "Exercise progress chart with weight per session and the next suggested weight", "세션별 무게와 다음 추천 무게가 보이는 종목 성장 차트", 1299),
         items=[
             ("Progressive overload", "증량 추천", "Hit your target reps on every set and it tells you to go heavier next time.", "모든 세트에서 목표 횟수를 채우면 다음번에 무게를 올리라고 알려줘요."),
             ("Learns your steps", "기구마다 다른 증량 단위", "It learns each machine's weight steps from your history. You can also type the weight yourself.", "기록에서 기구마다 다른 증량 단위를 배워요. 무게 칸을 직접 적을 수도 있어요."),
             ("Available weights", "가진 무게 설정", "Only have 12 kg dumbbells? Enter 12. At your top weight it suggests more reps instead.", "덤벨이 12kg뿐이면 12만 적어 두세요. 최고 무게에선 횟수를 늘리라고 알려 줘요."),
             ("Heavier day, fewer reps", "무게를 올린 날은 횟수를 낮춰서", "On days you go heavier, suggested reps drop to match.", "무게를 올린 날은 횟수를 알맞게 낮춰서 추천해요."),
             ("Progress chart", "종목별 성장 차트", "See how every exercise has climbed, session by session.", "종목마다 무게가 얼마나 늘었는지 한눈에 봐요."),
         ]),
    dict(id="plan", title=("Plan your week", "일주일을 계획해요"),
         lead=("Routines by weekday, built for you or by you.", "요일별 루틴을 직접 만들거나 추천받아요."),
         img=("mm-weekly", "Weekly tab listing a routine under each weekday", "요일마다 루틴이 나열된 주간 탭", 1299),
         items=[
             ("Weekday-first", "요일 중심 화면", "Tap a day to see that day's workout.", "요일을 누르면 그날 운동이 바로 보여요."),
             ("Routine builder", "루틴 추천", "Pick your days, session length and split to get a weekly plan. It fills empty days only by default.", "요일, 운동 시간, 분할만 고르면 요일별 루틴을 짜 줘요. 빈 요일만 채우는 게 기본이에요."),
             ("155 built-in exercises", "종목 155개 기본 목록", "Search with gym slang and the muscle group fills in for you.", "‘사레레’ 같은 줄임말로 찾고 부위도 자동으로 채워져요."),
             ("My Gym", "내 헬스장", "Add the equipment you have once and suggestions use it.", "있는 기구를 한 번 등록하면 추천에 반영돼요."),
             ("Two workouts a day", "하루 두 번 운동", "Add a Part 2, like a treadmill run.", "2부로 러닝머신이나 다른 루틴을 추가해요."),
             ("Edit freely", "자유롭게 편집", "Change routines and your weekly schedule any time.", "루틴과 요일을 언제든 자유롭게 바꿔요."),
         ]),
    dict(id="workout", title=("During the workout", "운동하는 동안"),
         lead=("One tap per set. The timer starts by itself.", "세트를 마치면 버튼 한 번, 타이머가 바로 시작돼요."),
         img=("mm-rest", "Rest timer with big numbers counting down between sets", "세트 사이를 큰 숫자로 세는 휴식 타이머", 1299),
         items=[
             ("Big rest timer", "큰 숫자 휴식 타이머", "Big numbers, and a notification when the rest is over.", "큰 숫자로 보이고, 끝나면 알림이 와요."),
             ("Swap mid-workout", "운동 중 바꾸기", "Just for today if someone is using the machine, or in the routine too if your gym doesn't have it.", "누가 쓰고 있으면 오늘만, 기구가 없으면 루틴에서도 바꿔요."),
             ("Treadmill log", "러닝머신 기록", "Time, speed and incline, a big stopwatch and estimated calories.", "시간·속도·경사, 큰 스톱워치, 대략 칼로리."),
             ("Undo the last set", "방금 넣은 세트 취소", "Logged the wrong set? Take it back.", "잘못 넣은 세트는 바로 취소해요."),
         ]),
    dict(id="history", title=("Look back", "돌아보기"),
         lead=("Every workout is remembered.", "운동은 모두 기억해요."),
         img=("mm-history", "History tab with a four-week calendar and records for each exercise", "4주 달력과 종목별 기록이 있는 기록 탭", 1299),
         items=[
             ("4-week calendar", "4주 달력", "See at a glance which days you trained.", "운동한 날이 한눈에 보여요."),
             ("History by routine", "루틴별 기록", "Your history is grouped by routine.", "루틴별로 기록이 쌓여요."),
             ("Muscle report", "부위별 리포트", "Weekly sets for each muscle group, and alerts for groups that have stalled.", "주간 세트 수와 정체된 부위를 알려 줘요."),
         ]),
    dict(id="habit", title=("Stay consistent, stay private", "꾸준히, 그리고 안전하게"),
         lead=("A small nudge when you skip. Nothing leaves your iPhone.", "쉬는 날이 길어지면 살짝 알려줘요. 기록은 아이폰 밖으로 나가지 않아요."),
         img=None,
         items=[
             ("Friendly nudges", "근손실 전에 알림", "A reminder when you skip too many days. You can turn it off.", "쉬는 날이 길어지면 알려줘요. 끌 수 있어요."),
             ("A mascot app icon", "캐릭터 앱 아이콘", "The icon looks worried when you skip more than 3 days.", "3일 넘게 쉬면 걱정하는 얼굴로 바뀌어요."),
             ("8 languages", "8개 언어", "English, Korean, Japanese, Traditional Chinese, German, Spanish, French and Portuguese.", "한국어·영어·일본어·중국어(번체)·독일어·스페인어·프랑스어·포르투갈어."),
             ("No account, no ads", "가입도 광고도 없어요", "Your workouts stay on your iPhone. No sign-up, no tracking, no ads.", "모든 기록은 내 아이폰에만 저장돼요. 로그인, 추적, 광고가 없어요."),
         ]),
]

MUSCLEMEMORY_FAQ = [
    ("How do I change exercises in a routine?", "루틴의 종목은 어떻게 바꾸나요?",
     "Open the Weekly tab and tap a routine under any day. You can add, remove or reorder exercises and set sets and reps.",
     "주간 탭에서 요일 아래 루틴을 누르면 종목 추가·삭제·순서 변경과 세트·횟수 설정을 할 수 있어요."),
    ("Can I do a different routine today?", "오늘만 다른 루틴을 할 수 있나요?",
     "Yes. Open the Today tab, tap another weekday at the top, then use “Change or add today's workout”. It changes today only and your routine stays the same.",
     "네. 오늘 탭 위쪽에서 다른 요일을 누른 뒤 ‘오늘 운동 바꾸기·추가’를 누르세요. 오늘만 바뀌고 루틴은 그대로예요."),
    ("The machine is busy, or my gym doesn't have it.", "기구가 사용 중이거나 헬스장에 없어요.",
     "Tap Swap on the exercise during your workout. Choose today only, or replace it in the routine as well.",
     "운동 중 그 종목의 ‘바꾸기’를 누르세요. 오늘만 바꾸거나 루틴에서도 바꿀 수 있어요."),
    ("How does it choose the next weight?", "다음 무게는 어떻게 정하나요?",
     "When you hit your target reps on every set, it suggests going heavier next time. It learns each machine's step from your history. If you only have certain weights, such as 12 kg dumbbells, set them under Available weights. At your top weight it suggests more reps instead.",
     "모든 세트에서 목표 횟수를 채우면 다음에 무게를 올리라고 알려줘요. 기구마다 증량 단위는 기록에서 배워요. 12kg 덤벨처럼 가진 무게가 정해져 있으면 ‘가진 무게’에 적어 두세요. 최고 무게에서는 횟수를 늘리라고 알려줘요."),
    ("Can it build a routine for me?", "루틴을 대신 짜 주나요?",
     "Yes. Open the Weekly tab and tap Suggest a routine. Pick your days, session length and split. Add your gym's equipment once in My Gym under Settings. By default it fills empty days only, and days that already have a routine stay as they are.",
     "네. 주간 탭에서 ‘루틴 추천’을 누르고 요일, 운동 시간, 분할을 고르세요. 설정의 ‘내 헬스장’에 있는 기구를 한 번 등록해 두면 돼요. 기본은 빈 요일만 채우고, 이미 루틴이 있는 요일은 그대로 둬요."),
    ("Why does it ask for notifications?", "왜 알림 권한을 묻나요?",
     "To tell you when your rest timer ends and to nudge you on workout days. You can turn nudges off in Settings. Notifications are created on your iPhone; nothing is sent to a server.",
     "휴식 타이머가 끝났을 때와 운동하는 날 깜빡하지 않게 알려주기 위해서예요. 운동 알림은 설정에서 끌 수 있어요. 알림은 아이폰 안에서 만들어지고 서버로 보내는 건 없어요."),
    ("Is my workout history backed up?", "운동 기록이 백업되나요?",
     "Your history is stored only on your iPhone. The app has no backup or sync feature, so deleting the app deletes it.",
     "기록은 아이폰에만 저장돼요. 앱에는 백업이나 동기화 기능이 없어서 앱을 삭제하면 기록도 함께 지워져요."),
]

# ---------------------------------------------------------------- page chrome
HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}<link rel="stylesheet" href="../style.css">
<script>(function(){{var s=localStorage.getItem('lang');var l=s||((navigator.language||'en').toLowerCase().indexOf('ko')===0?'ko':'en');document.documentElement.setAttribute('data-lang',l);window.toggleLang=function(){{var n=document.documentElement.getAttribute('data-lang')==='ko'?'en':'ko';document.documentElement.setAttribute('data-lang',n);localStorage.setItem('lang',n)}}}})()</script>
</head>
<body>
<nav class="gnav"><div class="in">
<a class="mark" href="../index.html">dudulabs</a>
<a class="app" href="../daycount/"><span lang="en">DayCount</span><span lang="ko">데이카운트</span></a><a class="app" href="../musclememory/"><span lang="en">Muscle Memory</span><span lang="ko">머슬메모리</span></a>
<button onclick="toggleLang()"><span lang="en">한국어</span><span lang="ko">English</span></button>
</div></nav>
<main>"""

FOOT = """</main>
<footer><div class="in">
<span>© 2026 dudulabs · duhyun jo</span>
<span><a href="../privacy.html"><span lang="en">Privacy Policy</span><span lang="ko">개인정보처리방침</span></a><span class="sep">|</span><a href="mailto:dudulabs.dev@gmail.com">dudulabs.dev@gmail.com</a></span>
</div></footer>
</body>
</html>
"""


def hero(app):
    d = app
    return (
        f'<section class="tile {d["tone"]} has-shots"><img class="icon" src="../assets/apps/{d["icon"]}" alt="{d["name_en"]} icon">'
        f'<h1>{T(d["name_en"], d["name_ko"])}</h1><p class="tag">{T(*d["tag"])}</p>'
        f'<div class="links"><a class="pill" href="mailto:dudulabs.dev@gmail.com?subject={d["subject"]}">{T("Contact support", "문의하기")}</a>'
        f'<a class="more" href="privacy.html">{T("Privacy", "개인정보처리방침")}</a></div>'
        f'<p class="note"><a class="store" href="https://apps.apple.com/app/id{d["id"]}">{T("Download on the App Store", "App Store에서 받기")}</a></p>'
        f'<div class="shots-wrap"><div class="shots">'
        f'<img lang="en" src="../assets/features/{d["hero"]}-en.webp" width="560" height="1216" alt="{html.escape(d["hero_alt"][0])}" loading="lazy">'
        f'<img lang="ko" src="../assets/features/{d["hero"]}-ko.webp" width="560" height="1216" alt="{html.escape(d["hero_alt"][1])}" loading="lazy">'
        f'</div></div></section>\n'
    )


def band(b, idx, flip=False):
    parch = " parch" if idx % 2 else ""
    has_img = b.get("img")
    cls = "band" + parch + (" pics" if has_img else " noimg")
    if has_img and flip:
        cls += " flip"
    items = "".join(
        f'<div><dt>{T(h_en, h_ko)}</dt><dd>{T(l_en, l_ko)}</dd></div>' for h_en, h_ko, l_en, l_ko in b["items"]
    )
    copy = f'<div class="copy"><h2>{T(*b["title"])}</h2><p class="lead">{T(*b["lead"])}</p><dl>{items}</dl></div>'
    pic = ""
    if has_img:
        name, a_en, a_ko, h = b["img"]
        pic = f'<div class="pic">{img_pair(name, a_en, a_ko, folder=b.get("folder", "features"), h=h)}</div>'
    return f'<section class="{cls}" id="{b["id"]}"><div class="wrap">{copy}{pic}</div></section>\n'


def faq(items, idx, app):
    parch = " parch" if idx % 2 else ""
    det = "".join(
        f'<details><summary>{T(q_en, q_ko)}</summary><p>{T(a_en, a_ko)}</p></details>' for q_en, q_ko, a_en, a_ko in items
    )
    return f'<section class="band noimg small{parch}" id="faq"><div class="wrap"><h2>{T("Questions", "자주 묻는 질문")}</h2><div style="margin-top:18px">{det}</div></div></section>\n'


def support(idx, app):
    parch = " parch" if idx % 2 else ""
    return (
        f'<section class="band noimg small{parch}" id="support"><div class="wrap"><h2>{T("Support", "지원")}</h2>'
        f'<p style="color:var(--muted);margin-top:18px">{T("Something not working? Email us with your iPhone model and iOS version.", "문제가 있으면 아이폰 모델과 iOS 버전을 같이 적어 메일 주세요.")}</p>'
        f'<p style="margin-top:12px"><a href="mailto:dudulabs.dev@gmail.com?subject={app["subject"]}">dudulabs.dev@gmail.com</a></p></div></section>\n'
    )


DAYCOUNT = dict(
    id="6834637942", name_en="DayCount", name_ko="데이카운트", icon="daycount.png", tone="parch", subject="DayCount%20support",
    tag=("Countdown widgets for the days that matter.", "중요한 날을 홈 화면 위젯으로."),
    hero="hero-dc-widgets", hero_alt=("DayCount widgets in small, medium and large sizes", "소형·중형·대형 데이카운트 위젯"),
    title="DayCount — dudulabs", desc="Countdown widgets for the days that matter.",
)
MUSCLEMEMORY = dict(
    id="6834974384", name_en="Muscle Memory", name_ko="머슬메모리", icon="musclememory.png", tone="dark", subject="Muscle%20Memory%20support",
    tag=("A gym log that tells you what to lift next.", "다음에 몇 kg 들지 알려주는 운동 기록."),
    hero="hero-mm-today", hero_alt=("Muscle Memory Today tab with the day's workout and a Finish set button", "오늘의 운동과 세트 완료 버튼이 있는 머슬메모리 오늘 탭"),
    title="Muscle Memory — dudulabs", desc="A gym log that tells you what to lift next.",
)


def page(app, bands, faqs, robots=""):
    out = HEAD.format(title=app["title"], desc=app["desc"], robots=robots) + "\n" + hero(app)
    n_img = 0
    for i, b in enumerate(bands):
        out += band(b, i, flip=bool(b.get("img")) and n_img % 2 == 1)
        n_img += 1 if b.get("img") else 0
    out += faq(faqs, len(bands), app)
    out += support(len(bands) + 1, app)
    return out + FOOT


def main():
    (SITE / "daycount/index.html").write_text(page(DAYCOUNT, DAYCOUNT_BANDS, DAYCOUNT_FAQ), encoding="utf-8")
    (SITE / "musclememory/index.html").write_text(page(MUSCLEMEMORY, MUSCLEMEMORY_BANDS, MUSCLEMEMORY_FAQ), encoding="utf-8")
    print("wrote daycount/index.html, musclememory/index.html")


if __name__ == "__main__":
    main()

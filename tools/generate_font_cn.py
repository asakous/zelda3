#!/usr/bin/env python3
"""Generate font_cn.png for zelda3 Chinese language support.

Creates a bitmap font image with 16x16 pixel CJK characters arranged in a grid.
The image uses palette mode with 4 colors (matching 2BPP SNES format):
  0 = transparent, 1 = color1, 2 = color2, 3 = color3

Layout:
  - 32 characters per row
  - First 112 entries: Latin/symbol characters (from US font, reused in encode_font_cn)
  - Remaining entries: 1118 CJK characters at 16x16

This script only generates the CJK portion. The US font portion is handled
by encode_font_cn() which reads from the existing US font.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'assets'))

from PIL import Image, ImageFont, ImageDraw

# The sorted CJK characters from dialogue_cn.txt
CJK_CHARS = list(
  '一七萬三上下不與專且世東丟兩個中豐臨為主麗舉久麼義之乎樂也書買亂了予爭事於虧互井亞些亡交產亮親人什仇今仍從仔他付代令以們件價任份仿企伏伐休眾優夥會偉傳傷伴伸似但位住佐體何佛作你使供儂便保信倒候借值假做停健偷儲像兒允充先光克免兔入全公六共關興兵其具茲內再冒冰沖冷凍準減凝幾憑兇出擊刃分切劃列則創利別刮到制刺刻前劍劇剩副劈力辦功加務動助勵勁勞勢勇勉勾匙匠升午半單賣南卜占卡盧卦衛印危即厄廳歷厚原去又及友雙反發取受變口古另叨只叫召可右吃各合吉吊同名後向嗎吞否吧聽啟吱吵吸吹呀呃告員呢呣周呱呼命和咒哢咕咳咻品哇哈響喲哥哦哪哼嘮喚唯商啊啦喂喜喝嗝嗯嘛嘟嘿嚕器噬囚四回因團圍國圖土聖在地場壞塊堅墜坦型埋城堂堡塔塘塞墓墻增壁士聲處備覆外多夠大天太夫失頭奪奇奏獎套女她好如姆始姿婆子字存孫學孩它守安完官定宜寶實寵客室宮害家容寄密寒對尋封射將小少爾嘗就尼盡局層居展屬山巖巢工左巧巨差己已布師希帶幫常幹平年並幸廣莊慶應底店座庭康建開棄弄式弓引弟張彌弱彈強當形影徹往征待很徊律得徘御德徽心必忘忙快懷態怎怕思怪總恐恢恭息惡情驚惑惜惠憊想惹意感愧願慧慰憾懂懦戲成我或戰房所扇手才打扔托扛扭扯擾找承技把抓投撫搶護報抱抵擔拉拔拖招拜擁擇拯拾拿持指按挑挖擋揮捕換搗據掉掘探接控推掩擲描提揭搜搞搬攜摧摸撞擅操攀攢支收改攻放故敵救教敢散數整文鬥料斷斯新方旁旅旋族無既舊早時明易映是暈晚晨普晶智暖暗暴曦曲更曾替最月有朋服望期木未本機殺桿村杖束條來松林枚果枝架某查標樹樣根格樁梭棋棒森棵樓概模橫次歡欲欺歉止正此步武死殿毀每比毛氏民氣水永求池汪沈沙沒河治沼沿泉泊法注泰澤灑洞活派流浪海消湧渦深混清遊湖湛滾滿漆漠漩漫潛澈激瀑灌火滅燈靈災炎炸點煉爛烈煩熱焰然照熬燃爆爪愛父爽片牌牢物牽特犯狂獨猩獻猴王瑪玩環現珍珠球理瓦瓶甚甜生用由甲界留疑疲病痛登白百的皮益蓋盜盛目直相盼盾看真眠眩眼著睛睡瞄瞌矗知石砍破砸確礙碎碑示禮祈祝神祭禱禁福離種科秒秘積稱移稀稍穆穴空穿突窩立站竟章笛第籠等答策簡算管箭箱篷類粉精糊糟系索緊繁紅約級紀納縱線細終經綁結繞給絕統繼績續綠緝縮缺罐網罩罪置美群老者而耗聊聯聚肉股肯胖勝能脈腳臉腿臂自至致舒舞色節花英蕩榮藥獲莽菇薩落蒙蓄藍蔽蘊藏蘑蟲蛋蟄蜂蜜血行衣表被裂裝裔西要見觀視覺角解觸言計認讓議記講訝許論設訪證識訴試誠話該語誤說請諾讀誰調謀謊謂謝負賢敗貪購貴費賊資賞賜賺贏赫走趕起趁越趣足跑跟路跳踢蹦蹼身躲輕輩輝輸邊達過迎運近還這進遠連述迷追退送逃選途通逛逝造遇遍道遺遭避那邦邪部都配酷釋里重量金針鑰鉤錢鐵鎧鏟銀鋪鏈鎖錯錘鍵鍛鏢鏡長門閃閉問闖閒間聞陰陣阿附陳降院除險陪陶隨隱難雄集雨霧需震非靠面靴音頂順須顧預領顆題顏風飛飾香馬驅騎騙騷骨骷髏高鬼魂魔魚魯鳥麻黃黑鼾齊龜託裡註復禦沉隻製迴斗鬆佈彷彿盪衝划係游颳傢伙咔瀰牆藉慾矇凶'
)

# CN punctuation characters (positions 96-111 in the alphabet)
CN_PUNCT = ['，', '。', '！', '？', '…', '：', '、', '—', '（', '）', '《', '》', '\u201c', '\u201d', '\u2018', '\u2019']

CHARS_PER_ROW = 32
CELL_SIZE = 16
FONT_PATH_DEFAULT = '/System/Library/Fonts/STHeiti Medium.ttc'
FONT_SIZE_DEFAULT = 12

# Ark Pixel 12px - pixel-perfect bitmap font for retro games (SIL OFL license)
FONT_PATH_PIXEL = os.path.join(os.path.dirname(__file__), '..', 'tables', 'ark-pixel-12px-zh_cn.otf')
FONT_SIZE_PIXEL = 12


def generate_font_cn(output_path):
  """Generate the CJK font image.

  The image contains CN punctuation (16 chars) + CJK chars (1118) = 1134 chars total.
  These map to alphabet positions 96-111 (punct) and CJK indices 0-1117.
  """
  all_chars = CN_PUNCT + CJK_CHARS
  num_chars = len(all_chars)
  num_rows = (num_chars + CHARS_PER_ROW - 1) // CHARS_PER_ROW

  img_w = CHARS_PER_ROW * CELL_SIZE
  img_h = num_rows * CELL_SIZE

  # Create grayscale image, render, then threshold to 1-bit
  img = Image.new('L', (img_w, img_h), 0)
  draw = ImageDraw.Draw(img)

  # Use pixel font if available, fall back to system font
  if os.path.exists(FONT_PATH_PIXEL):
    font = ImageFont.truetype(FONT_PATH_PIXEL, FONT_SIZE_PIXEL)
    print(f'Using pixel font: {FONT_PATH_PIXEL}')
  else:
    font = ImageFont.truetype(FONT_PATH_DEFAULT, FONT_SIZE_DEFAULT)
    print(f'Using system font: {FONT_PATH_DEFAULT}')

  for i, ch in enumerate(all_chars):
    col = i % CHARS_PER_ROW
    row = i // CHARS_PER_ROW
    x = col * CELL_SIZE
    y = row * CELL_SIZE

    # Get bounding box to center the character
    bbox = font.getbbox(ch)
    char_w = bbox[2] - bbox[0]
    char_h = bbox[3] - bbox[1]

    # Center horizontally, align to top with small offset
    dx = (CELL_SIZE - char_w) // 2 - bbox[0]
    dy = (CELL_SIZE - char_h) // 2 - bbox[1]

    draw.text((x + dx, y + dy), ch, fill=255, font=font)

  # Threshold to binary body mask, then dilate to create outline
  pixels = img.load()

  # Step 1: Create binary body mask
  body = [[pixels[px, py] > 80 for px in range(img_w)] for py in range(img_h)]

  # Step 2: Dilate body by 1 pixel to get outline region
  dilated = [[False] * img_w for _ in range(img_h)]
  for py in range(img_h):
    for px in range(img_w):
      if body[py][px]:
        for dy in range(-1, 2):
          for dx in range(-1, 2):
            ny, nx = py + dy, px + dx
            if 0 <= ny < img_h and 0 <= nx < img_w:
              dilated[ny][nx] = True

  # Step 3: Assign colors — body=2 (white), outline only=1 (blue)
  palette_img = Image.new('P', (img_w, img_h))
  palette_pixels = palette_img.load()

  for py in range(img_h):
    for px in range(img_w):
      if body[py][px]:
        palette_pixels[px, py] = 2  # White body
      elif dilated[py][px]:
        palette_pixels[px, py] = 1  # Blue outline
      else:
        palette_pixels[px, py] = 0  # Transparent

  # Set a simple palette (similar to existing font PNGs)
  pal = [0] * 768
  # Color 0: transparent (background gray)
  pal[0], pal[1], pal[2] = 192, 192, 192
  # Color 1: light
  pal[3], pal[4], pal[5] = 128, 128, 128
  # Color 2: medium
  pal[6], pal[7], pal[8] = 64, 64, 64
  # Color 3: full
  pal[9], pal[10], pal[11] = 0, 0, 0
  palette_img.putpalette(pal)

  palette_img.save(output_path)
  print(f'Generated {output_path}: {img_w}x{img_h}, {num_chars} characters ({len(CN_PUNCT)} punct + {len(CJK_CHARS)} CJK)')


if __name__ == '__main__':
  output = os.path.join(os.path.dirname(__file__), '..', 'tables', 'font_cn.png')
  if len(sys.argv) > 1:
    output = sys.argv[1]
  generate_font_cn(output)

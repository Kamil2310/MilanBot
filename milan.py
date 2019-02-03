"""
Created on Sat Feb  2 06:19:13 2019
@author: ACU
Milan Bot
"""

import os, random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps
import textwrap

##############################################################################
def dashinsert(str, insertion):
    
    length = len(str)
    position = random.randint(0,length)
    return str[:position] + insertion + str[position:]
##############################################################################
def fix_text(text):
    
    text = text.replace("\n\n","")
    text = text.replace(".","")
    text = text.replace(",","")
    text = text.split()
    return text

##############################################################################
def random_milan(text, word_filter, max_words):
    if len(text)>20:
        text = fix_text(text)
    location = os.getcwd()
    file_name_list = []
    text_to_picture = []
    x = random.randint(1, max_words)
    font_size = 72
    TRANSPARENCY = 30
    
    for folderName, subfolders, filenames in os.walk(location):
        file_name_list.extend(filenames)
        file_name_list = [sent for sent in file_name_list if not any(word in sent for word in word_filter)]
        
    for i in range(x):
       text_to_picture.append(text[random.randint(0, len(text)-1)]) 
       
    text_to_picture = ' '.join(text_to_picture)
    if len(text)>20:
        text_to_picture = dashinsert(text_to_picture, ' milan ')
        text_to_picture = dashinsert(text_to_picture, ' siempre ')
    text_to_picture = textwrap.wrap(text_to_picture, width=15)
    
    img = Image.open(file_name_list[random.randint(0, len(file_name_list)-1)])
    logo = Image.open('logo.png')
    logo_w, logo_h = logo.size
    logo = ImageOps.fit(logo, (60, 100), Image.ANTIALIAS)
    logo_w, logo_h = logo.size
    img_w, img_h = img.size
    logo_pos = img_w - logo_w, img_h - logo_h
    draw = ImageDraw.Draw(img)
    font_pic = ImageFont.truetype("comic.ttf", font_size)
    font_sign = ImageFont.truetype("comic.ttf", 48)
    current_h, pad = img_h - font_size*(len(text_to_picture)+1)*1.4, 10   
    for line in text_to_picture:
        w, h = draw.textsize(line, font=font_pic)
        draw.text(((img_w - w) / 2, current_h), line, font=font_pic)
        current_h += h + pad
    draw.text(((img_w - w) / 2, current_h), '      "Miño Piątek Molnár"', font=font_sign)
    
    if logo.mode!='RGBA':
        alpha = Image.new('L', logo.size, 255)
        logo.putalpha(alpha)
    paste_mask = logo.split()[3].point(lambda i: i * TRANSPARENCY / 100.)
    img.paste(logo, logo_pos, mask=paste_mask)   
    img.save('milan.png')
##############################################################################      
text = '''Lorem ipsum dolor sit amet, cum an minim similique, duo vidisse integre volutpat no, his posse tamquam quaeque ut. Eu per solum oblique, vix at ferri nulla, sit no postea tibique explicari. Nec ad copiosae insolens scribentur, eum meis quas assueverit ex. Te mel zril nostro deleniti, pri ne virtute ancillae, oportere quaerendum at per. An cum discere reprimique.

Agam veri nec eu. Te vis nihil gloriatur, melius sententiae ad pro, no mei discere vocibus vulputate. Mel case everti eu, affert electram eos id. Te esse simul sea. Mei discere noluisse ad, nulla saperet ad vel.

Cum similique abhorreant ea, integre tibique usu an. Omnium iisque nec id. Ex ius errem instructior, odio voluptaria constituto cu nam. Mea erat percipitur et, ut quem legere petentium quo. Erat debet intellegam cu sit, meis quaeque delicatissimi ut vel.

Sed nibh erant iracundia id, in est clita aliquid principes. Erant mentitum oportere ut nam, in vis wisi splendide. Ut ius dicta pertinacia repudiandae. Cu ius posse aeque, cum assum menandri ad. Per ut civibus appareat accommodare.

Wisi audiam dolorum no duo, sit ne eros conclusionemque. Eirmod definiebas ex sed, an nec homero debitis. Vim simul argumentum eu, lucilius eleifend est eu, vel ignota timeam conceptam ne. Aeque audiam aeterno vix no, ponderum gloriatur sea ea.

No reprimique temporibus has, cu vix persius eloquentiam. Ne ius oratio consul partiendo, quo ne diceret detracto nominavi. Ea mea clita singulis, iisque facilisi eu qui. At eos omnis electram partiendo. Debitis fastidii dissentiunt usu no, cu has posse euripidis comprehensam.

Ea eos nihil aeterno, ne vix melius recteque vulputate. Ei quem omittantur conclusionemque cum, vix eu aeque civibus scripserit. Dicant periculis argumentum no sit, soluta erroribus necessitatibus te eum. Eam et probo postea.

Te pri erat blandit adolescens. Cibo fastidii qualisque eum ea. Ut quo congue nonumes, usu no harum mediocritatem. Eum id iisque senserit corrumpit. Mel ex nulla dissentiet, ea usu veniam singulis repudiandae.

Unum vitae latine ex mea. Id cum magna suscipit. Cum at suavitate iracundia persecuti, usu falli aliquid ut. Docendi percipit mea in, illud facilisis et usu. In adhuc dicunt appellantur ius, est an mutat mazim expetendis, detraxit pertinax mel ei.

Vis no vitae diceret. Quot euismod his ex. An nec altera nominavi, facilisi voluptatum mel ea. Cu habeo reque nostrum sit, mel assum verear eu. Aliquam debitis adversarium vix id, eum te docendi fastidii apeirian.'''

text_chamko = ['Calcio',
'La Mia vita',
'Per sempre',
'Milanisti',
'Milan',
'Merda juve',
'Tutti',
'Buono natale',
'Auguro',
'Supercopa',
'I ladri',
'Forza',
'Ti amo',
'La vittoria',
'É nostra']

max_words = 7
word_filter = ['.py', '.png']
random_milan(text_chamko, word_filter, max_words)

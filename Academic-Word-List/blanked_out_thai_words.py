# blanked_out_thai_words.py - 

# blank out a given Thai word 
# in a given Thai sentence
# slightly different from English
# since no inflection, such as: injure -> injuring 
# and no space between Thai words 

import re, sys 

def blankout_thai_word_in_sentence(word, sentence):
    pattern = r'{}'.format(word)
    regex = re.compile(pattern, re.UNICODE)
    return regex.sub('_______', sentence)
    

sentences = [
    ['บทคัดย่อ', 'ผลการศึกษาดังกล่าวนี้ได้รับรางวัลบทคัดย่อการศึกษาวิจัยยอดเยี่ยม'],
    ['สั่งสม', 'นายกรัฐมนตรีกำลังสั่งสมอำนาจโดยไม่มีผู้ใดคอยเหนี่ยวรั้ง'],
    ['แม่นยำ', 'คณะผู้วิจัยหวังว่าได้พบวิธีที่ง่ายและแม่นยำเพื่อใช้ตรวจคัดมะเร็งลำไส้ใหญ่แล้ว'],
    ['ถูกต้อง', 'ผู้บัญชาการกล่าวว่าจะให้ข้อมูลที่ถูกต้อง'],
    ['บรรลุ', 'ขณะนี้ผู้ก่อการร้ายยังไม่บรรลุวัตถุประสงค์'],
    ['ยอมรับ', 'พล.ต. สมบัติยอมรับว่า สนใจ(กับ)ข้อเสนอของรัสเซีย']
]

import sys
f = open('output2.txt', 'w', encoding='utf-8')
sys.stdout = f

for s in sentences:
    word = s[0]
    sentence = s[1]
    blanked_sentence = blankout_thai_word_in_sentence(word, sentence)
    print(f"{word}: {sentence} => {blanked_sentence}")
    
sys.stdout = sys.__stdout__
    

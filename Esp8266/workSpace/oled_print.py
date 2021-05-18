import init_oled
oled=init_oled.oled
def text_list(txt_list):
  line=0
  oled.fill(0)
  for text_line in txt_list:
    oled.text(text_line, 0, line)
    line=line+10
  oled.show()
text_list(("cC","B"))

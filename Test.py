import re
line = 'light orange bags contain 1 dark maroon bag, 3 dim maroon bags, 5 striped green bags, 2 pale aqua bags.'
patt_2 = re.compile(' [0-9] ')
y = re.sub(patt_2, '', line)
print(y)

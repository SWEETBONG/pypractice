시작=int(input('write start colume(1-9):'))
끝=int(input('write ende colume(1-9):'))



출력가=''

for 앞 in range(2,10):
    for 뒷 in range(1,10):
        지금='{}*{}={}\n'.format(앞,뒷,앞*뒷)
        출력가=출력가+지금
       
        
print(출력가)
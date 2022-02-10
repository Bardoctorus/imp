#construction pieces for internal links
muoIL1 = '<a href="'
muoIL2 = '">'
muoIL3 = '</a>'
#internal link builder
def muoILMaker(link, text):
        IL = muoIL1+link+muoIL2+text+muoIL3
        return IL

#TODO make the external link contruction pieces and function

#TODO make the embed condtruction and function

#TODO make the markdown parser including custom symbols for external links



















#silly test bereich

thislink = muoILMaker('https://www.penis.com','womble')

print(thislink)



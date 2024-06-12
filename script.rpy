# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    transform flip:
        xzoom -1.0

    transform flipback:
        xzoom 1.0

    transform midleft:
        xalign 0.18
        yalign 1.0

    transform middle:
        xalign 0.5
        yalign 0.5

    transform middletop:
        xalign 0.5
        yalign 0.15

    transform abitsmaller:
        xzoom 0.4
        yzoom 0.4

    transform abiiitsmaller:
        xzoom 0.55
        yzoom 0.55

    transform behindcount:
        xalign 0.45
        yalign 0.5

init python:
    renpy.add_layer("bro", below="master") # this is a new function in 6.99.8 that allows us to add new layers in a much simpler manner

screen countertop():
    # image "images/arrow.png" at arroww
    image "images/countertop.png" 

define vamp = Character("Камилла", color="#ecd0d0")
define me = Character("Я", color="#f3e48f")
image dimmedbg = "#000000AA" 
image dimmedscene = "#00000088" 
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bar1

    show screen countertop(_layer="bro") # shows screen on layer bglayer
    $ renpy.show_screen("countertop", _layer="bro")
    pause(4)
    show dimmedbg with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show vamp at behindcount with dissolve:
        abitsmaller
        

    # These display lines of dialogue.

    vamp "Хэй, милое местечко. Мне посоветовали сюда прийти."
    me "Спасибо! Для новеньких у нас один напиток бесплатно."
    vamp "Серьезно? Вот это сервис. И что же посоветует мне прекрасный бармен?"

    label drink_choise:
        menu:
            "Предложить кровавую Мэри и подмигнуть":
                show vamp smiling 
                me "У нас в меню есть кровавая Мэри по особому рецепту"
                jump bloody_mary
            "Предложить просто мохито":
                me "Мохито точно не разочарует"
                jump mojito
            "Дать барную карту":
                show vamp meh
                me "У нас все вкусное, можете выбрать на свой вкус"
                jump bar_menu

    label bloody_mary:
        vamp "А ты мне нравишься."
        me "Ха-ха, всё лучшее нашим посетителям."
        jump after_choise1

    label mojito:
        vamp "Надеюсь, алкогольный?"
        me "Даже не сомневайтесь."
        jump after_choise1
    
    label bar_menu:
        vamp "Хм, ну давай посмотрим..."
        vamp "Давай-ка кровавую Мэри."
        me "Сейчас всё будет."
        "Надо было предложить ее изначально, эх..."
        jump after_choise1


    label after_choise1:
        me "Всё готово."
        show vamp
        vamp "Спасибо, love."
        vamp "Расскажи, что у вас тут в баре вообще интересного бывает?"
        me "Ну..."

    label story_choise:
        menu:
            "Рассказать про бушующих пьяных оборотней":
                jump werewolfs
            "Рассказать, как фейри украшали бар":
                jump fairies

    label werewolfs:
        me "Мы недавно попали в новостные заголовки из-за товарещей-оборотней..."
        vamp "И по какому поводу?"
        me "Хах, тут легче просто показать фото."
        show dimmedscene with dissolve
        show werewolf_memo at middletop:
            abiiitsmaller
        pause
        hide werewolf_memo with dissolve
        hide dimmedscene with dissolve
        show vamp meh
        vamp "Ужас какой. Эти блохастые — позор мистического мира."
        me "Да тами просто люди хороши. Но мы все убрали, и начался новый день."
        show vamp
        vamp "Повезло, что не сравняли с землей."
        me "И то верно."
        jump after_choise2


    label fairies:
        me "Недавно у нас устраили целый весенний фестиваль фейри!"
        vamp "Ничего себе! А не осталось фото?"
        me "Сейчас покажу!"
        show dimmedscene with dissolve
        show fairy_memo at middletop:
            abiiitsmaller
        pause
        hide fairy_memo with dissolve
        hide dimmedscene with dissolve
        show vamp smiling
        vamp "Красота. Они всегда знают, как вернуть весну в душу."
        me "Однозначно."
        jump after_choise2

    label after_choise2:
        me "Не хотите еще чего-нибудь выпить?" 
        vamp "Спасибо, love, но, может, в следующий раз."
        me "Буду рада увидеть вас в следующий раз."
        hide vamp with dissolve
        pause(1)
        hide dimmedbg with dissolve
        
        "The End."

    # This ends the game.

    return

######################################################  MADE BY simple_human   

######################################################  DOWNLOADED FROM https://f95zone.to/threads/milfs-plaza-steam_14b-texic.66273/post-10356863

define mom = "{color=#e1bdff}Mom{/color}"     # [mom]
define son = "{color=#e5e349}Son{/color}"     # [son]
define dad = "{color=#3CABD3}Father{/color}"  # [dad]
define sis = "{color=#FF69B4}Sister{/color}"  # [sis]
define bro = "{color=#e5e349}Brother{/color}"  # [bro]

######################################################
init 1 python hide:

######################################################
    translate = renpy.translation.StringTranslator.translate

######################################################
    from re import compile

    smom = compile(r"(?i)stepmo(?:m|ther)") 
    mymom = compile(r"(?i)my (?:mom|mother)")
    odad = compile(r"(?i)your brother")

    br  = compile(r"(?i)brother")
    mbro = compile(r"(?i)(?<=my )brother")
    ybro = compile(r"(?i)(?<=your )brother")

    del compile

######################################################
    def current_node():
        namemap = renpy.game.script.namemap
        context = renpy.game.context
        def current_node():
            return namemap.get(context().current, None)
        try:
            return current_node
        finally:
            del current_node
    current_node = current_node()

##################
    def current_screen_name():
        current = renpy.current_screen
        default = ()
        def current_screen_name():
            return "_".join(getattr(current(), 'screen_name', default))
        try:
            return current_screen_name
        finally:
            del current_screen_name
    current_screen_name = current_screen_name()

    Say  = renpy.ast.Say
    Menu = renpy.ast.Menu 

######################################################
    def sim_hum_ipatch(self, t):
        t = translate(self, t)
        n = renpy.game.script.namemap.get(renpy.game.context().current)

################## Prologue 
        t = t.replace("Think about your wife.","Think about Mom.")
        t = t.replace("Thanks, brother. I knew I could rely on you.","I knew I could rely on you.")
        t = t.replace("Hey, you want me to look after your wife but at the same time","Hey, you want me to look after Mom, but at the same time")

        t = t.replace("Just don't let me down, brother.","Just don't let me down, Son.")
        t = t.replace("Brother…","Father…")
        t = t.replace("your older brother is a badass super-agent in the service of the government","your Father is a badass super-agent in the service of the government")

        t = t.replace("climb as high as my brother did, I decided to dig down instead.","climb as high as my Father did, I decided to dig down instead.")
        t = t.replace("The money that my brother left me for the time he'd be away","The money that my Father left me for the time he'd be away")
        t = t.replace("And since I didn't want to bother Mary and ask her for some pocket money","And since I didn't want to bother Mom and ask her for some pocket money")

        t = t.replace("Brother, forgive me…","Father, forgive me…")

################## Mary 
        t = t.replace("This is my husband's brother. He lives with me while James is away on business.","He is my [son].")
        t = t.replace("Your friend and one of his friends, were trying","Your [son] and some of his friends, were trying")
        t = t.replace("As you can see, [mc] is not in jail yet.","As you can see, your [son] is not in jail yet.")
        
        t = t.replace("I'd like to believe that your husband's brother just made a mistake.","I'd like to believe that your [son] just made a mistake.")
        t = t.replace("I'm not your mother. You can just walk away right now.","You can just walk away right now.")
        t = t.replace("James trusts you.","Your [dad] trusts you.")

        t = t.replace("But I'm not stupid and I'm not blinded by «brotherly» love for you.","But I'm not stupid. I can see that you don't want to change for the better.")
        t = t.replace("I agreed to let you stay here only because my husband asked me to.","It breaks my heart, but I'll have to take decisive measures.")
        t = t.replace("I was, as you know, very fortunate to have her shelter me after the death of my parents.","I hope you understand that your stupid actions can have a negative impact on all of us.")

        t = t.replace("I wonder if it's okay that I watch her taking a bath?","I wonder if it's okay that I'm peeping in on my mother taking a bath?")
        t = t.replace("I'm just your brother's wife who craves for some attention.","I'm just your mother who craves for some attention.")
        t = t.replace("I just stood there, thinking about my husband brother's cock.","I just stood there, thinking about my [son]'s cock.")

        t = t.replace("I just shouldn't forget that she's my brother's wife.","I just shouldn't forget that she's my mother.")
        t = t.replace("but if I were James, I'd be counting","but if I were in my father's place, I'd be counting")
        t = t.replace("I could use a little attention from a friend.","I think a little attention from [son] wouldn't hurt.")

        t = t.replace("The stunning pussy of my brother's wife flooded my mind.","Her amazing pussy...  my mother's pussy... it's flooded my mind.")
        t = t.replace("It means [mc] is sexually attracted to me after all.","It means my [son] is sexually attracted to me after all.")
        t = t.replace("I think this little pervert is looking right at my pussy","I think my [son] is looking right at my pussy")

        t = t.replace("to do when your friend is constantly involved in murky","to do when your [son] is constantly involved in murky")
        t = t.replace("death possible than see your friend rot","death possible than see your [son] rot,")
        # t = t.replace("She'll probably think that her friend is a damn pervert!","She'll probably think that her [son] is a damn pervert!")
        
        t = t.replace("but I'm still just your friend, and you need to remember that.","but I'm still your mother, and you need to remember that.")
        t = t.replace("What were you doing in her bedroom?","What were you doing in your mother’s bedroom?")
        t = t.replace("how it goes when you live with someone","how it goes when you live with mother")
        
        t = t.replace("It could be some special day for your brother.","It could be some special day for your father.")
        t = t.replace("By the way, when was Mary born?","By the way, when was your [mom] born?")
        t = t.replace("You don't remember her birthday?!","You don't remember your [mom]'s birthday?!")
        
        t = t.replace("find out Mary's date of birth as soon","find out your [mom]'s date of birth as soon")
        t = t.replace("As soon as Mary and Christie leave the house,\n I'll try", "As soon as Mom and Christie leave the house,\n I'll try")
        t = t.replace("4. Enter your brother's date of birth in different variations.", "4. Enter your father's date of birth in different variations.")
        
        t = t.replace("going to be so kind as to «lend» your friend 100$.","going to be so kind as to «lend» your lovely [sis] 100$.")
        t = t.replace("Too bad. Is your guardian home?","Too bad. Is your mother at home?")
        t = t.replace("I have a little present for your friend here.","I have a little present for your mother here.")
        
        t = t.replace("You do know that my friend is married, right?","You do know that my mother is married, right?")
        t = t.replace("getting your «ward» off the police register.","getting your [son] off the police register.")
        t = t.replace("I promised Mary's brother to look after her but she's going","I promised father to look after [mom] but she's going")
        
        t = t.replace("I'm glad to have such a wonderful friend like you.","I'm glad to have such a wonderful [son].")
        t = t.replace("She's just your friend, nothing more. You damn pervert.","She's your [mom]! You damn pervert.")
        t = t.replace("Are you afraid my brother will find out about us?","Are you afraid that father will find out about us?")
        
        t = t.replace("So, your friend doesn't mind you fucking other girls.","So, your mother doesn't mind your naughty behavior?")
        t = t.replace("Your friend is getting all lonely waiting for you","Your mother is getting all lonely waiting for you")
        t = t.replace("by ogling your girlfriend and after that you run to a bathroom and quickly rub one out","while gazing at your mother and then secretly satisfying yourself in the bathroom")
        
        t = t.replace("Oh, we need your neighobr's panties.","Oh, we need your [sis]'s panties.")
        t = t.replace("be able to date your girlfriend with no problem.","be able to date your mother with no problem.")
        t = t.replace("Sure, sure. Then I'm his step-mother.","Sure, sure. Then I'm the Empress of the Universe.")
        
        t = t.replace("When I got here, your brother was trying to break down","When I got here, your father was trying to break down")
        t = t.replace("only witness, his own brother, who was at home","only witness, his own [son], who was at home")
        t = t.replace("My woman's huge mature tits. They are so delicious","My mother's huge mature tits. They are so delicious")

        t = t.replace("I'm such a fool. Why did I invite him in?!","I'm such a fool. Why did I invite my [son] in?!")
        t = t.replace("Oh, I know everything about you.","Oh, I know everything about my sweet [son].")
        t = t.replace("Especially if I spend this time with someone I love.","Especially if I spend this time my lovely [son].")

        t = t.replace("Yes, don't stop, honey!","Yes, don't stop honey, fuck your Mommy!")
        t = t.replace("reap what you saw, my love.","reap what you saw, [son].")
        t = t.replace("Marina?! You want Marina?!!","[mom]?! You want my [mom]?!")

        t = t.replace("What about your step-daughter?","What about your daughter?")
        t = t.replace("You dirty boy!","You dirty\u200B boy!")
        t = t.replace("dirty boy!","Son!")

        t = t.replace("Marina...","Mom...")
        t = t.replace("Damn it, Mariska!","Damn it, Mom!")
        t = t.replace("Marishka!","Mom!")

        # if n:
            # if (n.filename, n.linenumber) == ("core/comic_frame_v2.rpyc", 260):
                # t = t.replace("Mary","Mom")

################## Christy 
        t = t.replace("Christy, my friend, recommended","Christy, my [sis], recommended")
        t = t.replace("to upset your girlfriend, that's all.","to upset your mother, that's all.")
        t = t.replace("My friend, she is the one who inspired","My [sis], she is the one who inspired")

        t = t.replace("Are you so angry that you call your mother by her first name?","You're so angry just because of some coffee?")
        t = t.replace("She may not be your own mother, but she has been raising you all your life and did everything possible so that you do not need anything.","She may not be a saint, but she did everything possible so that you don’t need anything.")
        t = t.replace("And you're not my boyfriend!","And you're my [bro]!")

        t = t.replace("Thank you, [mc], you're an amazing friend!","Thank you, [mc], you're an amazing [bro]!")
        t = t.replace("You say that just to flatter me, since we're friends","You say that just to flatter me, because I'm your [sis].")
        t = t.replace("Well, first of all, she's the daughter of my brother's wife.","Well, first of all, because she's my [sis]?")

        t = t.replace("Adopted daughter, as far as I'm aware.","Yeah, that complicates things a bit.")
        t = t.replace("I suspect your brother would be against your... affair.","I suspect your parents would be against your... affair.")
    
        if t.strip() == "Stylized with a modern design Bloody Mary costume!": return t

        # t = t.replace("Mary barged", "Mom barged")
        t = t.replace("Alright, I understand why my brother would think this way.","Alright, I understand why brother would think this way.")
        t = t.replace("I may not be her daughter, but I'm sure she views herself as my mentor who cares about my future.", "What do you mean 'why'?")

        t = t.replace("And for good reason.", "She's still our mother.")
        t = t.replace("My parents are long dead and all I have is Mary.", "[dad] away more often than he's home. Actually, we were never truly essential to him.")
        t = t.replace("It was a real feat for her to take me in.", "[mom] practically raised us on her own.")

        t = t.replace("If you don't get off my boyfriend's dick right now","If you don't get off my brother's dick right now")

################## rest 
        t = t.replace("Yeah. And judging by everything he said, he's Mary's husband.","Yeah. And judging by everything he said he's very unhappy that you're sleeping with Mary.")
        t = t.replace("I didn't know you stole someone's wife.","I didn't know you were sleeping with your Mother.")
        t = t.replace("I don't care about someone's wife and who you fuck.","I don't care who you fuck.")

        t = t.replace("That's your roommate's name, right?","That's your sister's name, right?")
        t = t.replace("Ah... You mean Marina. Yeah, she's the most dear person to me","Ah... Yeah, she's the most dear person to me.")
        t = t.replace("I'm ready to do anything for Marina.","I'm ready to do anything for her.")

        t = t.replace("My life would have no meaning if Marina or Christie were gone.","My life would have no meaning if she or Christie were gone.")
        t = t.replace("Besides, Marina and Christie mean everything to me. They're the reason I keep fighting.","Besides, they're mean everything to me, they're the reason I keep fighting.")
        t = t.replace("It's just that Marina is a very jealous woman...","It's just that the woman who visits me is very jealous...")

        t = t.replace("You're as cocky as your brother, [mc].","You're as cocky as your [dad], [mc].")
        t = t.replace("She works for my brother James.","She works for my [dad].")
        t = t.replace("Your brother?","Your [dad]?")

        t = t.replace("And it's hard to imagine a man who wouldn't dream of having sex with two girls at once.","Even in my wildest fantasies, I never imagined I'd be having sex with [mom] and [sis] at once.")

        t = smom.sub("Mother", t)

##################
        node = current_node()
        if isinstance(node, Say):
            who = node.who
            if who == "extend":
                who = _last_say_who

            if who in ('"[gg]"', "'[gg]'", '"[player_name]"', "mc"):   
                t = t.replace("Marina", "[mom]")
                t = t.replace("Mariska", "[mom]")
                t = t.replace("Marishka", "[mom]")
                t = t.replace("Mary", "[mom]")

                t = t.replace("James", "[dad]")
                t = br.sub("[dad]", t)
                t = mbro.sub("[dad]", t)

            if who in ('"Кристи"', '"Christie"', "'Кристи'", "'Christie'", "crs"):  
                t = t.replace("Mariska", "[mom]")
                t = t.replace("Marishka", "[mom]")
                t = t.replace("Marina", "[mom]")
                t = t.replace("Mary", "[mom]")

                t = t.replace("James", "[dad]")
                t = mymom.sub("Mother", t)
                t = odad.sub("[dad]", t)

            if who in ('"Марина"', '"Mary"', "'Марина'", "'Mary'", "mar"):   
                t = ybro.sub("[dad]", t)
                t = t.replace("my friend","my [son]")

            if who in ('"Джеймс"', '"James"', "'Джеймс'", "'James'"):   
                t = br.sub("[son]", t)

            if who in ('"Kat"', '"Кэт"', "'Kat'", "'Кэт'"):   
                t = t.replace("your Mary","your [mom]")

##################
        elif isinstance(node, Menu):                
            t = t.replace("Mary","Mom")
            t = t.replace("Marina","Mom")
            t = t.replace("Mariska","Mom")
            t = t.replace("Marishka","Mom")

##################

        elif current_screen_name and not isinstance(node, Say):

            t = t.replace("Mary","Mom")
            t = t.replace("Marina","Mom")
            t = t.replace("Mariska","Mom")
            t = t.replace("Marishka","Mom")

            t = t.replace("James", "Father")
            t = t.replace("brother", "Father")

##################
        return t
    renpy.translation.StringTranslator.translate = sim_hum_ipatch
    del sim_hum_ipatch

######################################################

######################################################  MADE BY simple_human   

######################################################  DOWNLOADED FROM https://f95zone.to/threads/milfs-plaza-steam_14b-texic.66273/post-10356863

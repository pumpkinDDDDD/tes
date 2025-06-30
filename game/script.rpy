#plssemogaselsai

# The game starts here.
define MC = Character ("[MC]")    
define TSM = Character ("Rudy")
define YM = Character ("Nix")
define F = Character ("Friend")    
define C = Character ("Cashier")
define P = Character ("Professor")
define LS = Character ("Loud Stranger")
define FS = Character ("Friendly Stranger")  
define CS = Character ("Chill Stranger")
define QS = Character ("Quiet Stranger")  
define RP1 = Character ("Random Person 1")
define RP2 = Character ("Random Person 2")
define LL = Character ("Land Lord")
define GTWU = Character ("???")

image ed1ver1 = "images/ed1ver1.png"
image ed2ver1 = "images/ed2ver1.png"
image ed3ver1 = "images/ed3ver1.png"
image ed4ver1 = "images/ed4ver1.png"
image ed5ver1 = "images/ed5ver1.png"
image ed6ver1 = "images/ed6ver1.png"

image ed1ver2 = "images/ed1ver2.png"
image ed2ver2 = "images/ed2ver2.png"
image ed3ver2 = "images/ed3ver2.png"
image ed4ver2 = "images/ed4ver2.png"
image ed5ver2 = "images/ed5ver2.png"
image ed6ver2 = "images/ed6ver2.png"


label start:

"Choose your pronoun."
menu:
            "She":
                $ player_gender = "she"
                $ player_possessive = "her"
                $ player_object = "her"
                $ player_pronoun = "girlfriend"
                $ player_sb =  "is"
                $ player_ds =  "girl"
            "He":
                $ player_gender = "he"
                $ player_possessive = "his"
                $ player_object = "him"
                $ player_pronoun = "boyfriend"
                $ player_sb =  "is"
                $ player_ds =  "boy"
            "They":
                $ player_gender = "they"
                $ player_possessive = "their"
                $ player_object = "them"
                $ player_pronoun = "partner"
                $ player_sb =  "are"
                $ player_ds =  "person"

label start1:
    $ MC = renpy.input("What is Your Name?")
    
    $ TSM_route = 0
    $ YM_route = 0
    $ YM_dp = 0
    $ YM_ij = 0

    scene cg1 with fade
    MC  "(I can do this, just a bit more...)"                                
    scene black with fade
    pause 0.5 
    scene cg1 with fade                              
    MC "(What time is it...? I can barely tell anymore.)"                             
    scene black with fade
    pause 0.5 
    scene cg1 with fade                              
    MC "(I sure hope the sun isn’t coming up... Not yet please...)"                                
    MC "(I don’t think I'm even halfway done with this..)"                              
    scene black with fade
    pause 0.5 
    scene cg1 with fade                               
    MC "(I gotta pull through, I have too much to do.)"                              
    MC "(Must... continue.)"                             
    scene black with fade                            
    MC "(...)"                                
    play sound "audio/bird.mp3"                          
    MC "(...)"                              
    MC "(Huh? Is...is the sun up?)"                            
                            
    scene insidepr with fade
    play music "audio/normal.mp3" fadein 1.0
    MC "(I must’ve fallen asleep on my desk, I should probably save my progress from last night.)"                                
    MC "(Shit, it’s already 9?)"                           
    MC "(I overslept! I have class in an hour!)"                               
    MC "(No time for breakfast [MC], we gotta rush!)"                               
                            
    "Getting up from my seat, I can feel my bones creak as if I'm a neglected machine in some dusty old factory. My neck, my back, my shoulders, almost everything is starting to feel sore."                                
    MC "“Is this how my dad feels...?“"                              
    MC "“Yikes, I feel like I'm aging faster than my parents.“"                               
    MC "(Looking around my room, I feel a strange mix of disappointment, apathy and stress. I know I should’ve cleaned up a week or two ago, but I just feel so tired all the time recently.)"                              
    MC "(Reasonably, I know I should have a set a specific date and time to just do all this but I just never ended up doing it.)"                               
    MC "(The lack of deadlines with housework doesn't help either.)"                              
                            
                            
    MC "(I almost wish I had a maid to do all the basic housework that I haven’t bothered to do.)"                             
    MC "(It’d be nice to have someone sweep the floor or clean the bathroom while I struggle to type in front of my laptop.)"                                
    MC "(Maybe even cook me a nice warm meal, that’d save me some time.)"                               
    MC "(Yea, having a maid sounds really nice.)"                            
    MC "(What if I sneak in some cleaning time this morning? I might have enough time to atleast take my laundry to the laundromat?)"
    scene insidepr with vpunch
    play sound "audio/alarm.mp3"
    MC "(Or not! That’s my 'late alarm' ringing!)"
    MC "(You can do this [MC], if you hurry you can still get to campus on time!)"
    
    scene kosd with fade
    MC "(How much time do I have left?)"
    MC "(Okay, that’s not bad. With 20 minutes left, I don’t think I’d need to run to get to campus on time.)"

    show tsm sdangy
    "Before I head out the gate, I notice my downstairs neighbor Rudy coming out the door as well. He stares at me for a brief moment before looking away, seeming unsure of himself. "
    "Since we already made eye contact, I decided to walk up to him and talk to him."
    "He seems well, or at least well enough. To me, he seems like the type of person who would fare well against the hardships of college."
    MC "(I took a peek inside his place before we headed out to the campus orientation together, it seemed super clean.)"
    MC "(The fact that he didn't have a lot of things in his room helped a lot, it made me reconsider my own room for a moment)"
    show tsm silent:
        parallel:
            ease .5 zoom 1.3
        parallel:
            yalign 0.0
            linear 0.0 yalign 0.0 xalign 0.5

    MC "(Oh shit, did he not want me to come closer?)"
    MC "(Welp, too late now.)"

    show tsm silent:
        parallel:
            ease .5 zoom 1.5
        parallel:
            yalign 0.0
            linear 0.0 yalign 0.0 xalign 0.5
    MC "“Rudy?“"
    show tsm nuhsure
    TSM "“[MC]?“"
    show tsm nsilent
    MC "“Oh, hi! You headin’ out too?“"
    show tsm nnormal
    TSM "“Yea, I got class in like 20 minutes. I figured I'll walk while I still have time.“"
    MC  "“So do I actually, wanna walk together?“"
    show tsm nuhsure
    TSM "“Uh, sure?“"
    
    scene roadd with fade
    show tsm nsilent:
        parallel:
            ease .5 zoom 1.5
        parallel:
            yalign 0.0
            linear 0.0 yalign 0.0 xalign 0.5
    MC "“I haven’t seen you in a while.“"
    show tsm nuhsure
    TSM "“I haven’t seen you much either, has it been months?“"
    MC "“Definitely, how’s life treating you?“"
    show tsm nhappy
    TSM "“It could be worse, but since we got this far I guess we just gotta survive.“"
    show tsm nnormal
    TSM "“What about you? You seem tired.“"
    menu: 
                "I make do, it’s not that bad":
                    MC "(I’ve seen my classmates be busier so i’m probably not doing too bad for now)"
                    show tsm nhappy
                    TSM "“That’s good to hear.“"
                "Oh man, you can tell?":
                    "(Do I have under eye bags or something? Or is the stress just emanating from me?)"
                    show tsm nuhsure
                    TSM "“Sort of? I’ve been seeing you less frequently around here, so I assumed you were.“"
    show tsm nsilent
    MC "“Hmm“"
    MC "(I haven’t seen him around in a while but if there’s anything that stayed the same about him, it’s his scent)"
    MC "(He kinda smells like food, I guess he was cooking before leaving? Or atleast whatever it is, it smells good)"
    MC "“You smell good.“"
    show tsm nhuh
    TSM "“H-huh?“"
    show tsm ndeflecting
    TSM "“You tryin’ to do somethin?“"
    show tsm npout
    MC "“Nah, I’m just kinda hungry and you happen to smell like food, very tasty.“"
    show tsm nangy
    TSM "“Don’t sniff me! I just finished making lunch for myself before I went off.“"
    MC "“You’re still cooking everyday?“"
    show tsm nuhsure
    TSM "“Yea?  And you’re not?“"
    MC "“No? Do I look like I have the time?“"
    show tsm nnormal
    TSM "“Pretty sure you were making simple one pot pasta recipes back when we first met.“"
    show tsm nsilent
    MC "“Yea, that only lasted a whole month. My electric pot has been retired since.“"
    show tsm nuhsure
    TSM "“What? Then what have you been eating?“"
    show tsm nsilent
    MC "“I buy food from the food stalls, they’re pretty cheap.“"
    MC "“Or if  I have class I eat at the cafeteria. The food’s not bad y’know?“"
    show tsm nnormal
    TSM "“If you say so, I still think cooking for myself is better.“"
    MC "“Good for you, I think I've completely given up on it.“"
    TSM "“You should eat better.“"
    show tsm nsdbangy
    TSM "“Not that I care about you or anything.“"
    show tsm npout
    MC "“Uh huh, thanks anyway.“"
    
    menu: 
            "(Maybe I will try cooking again once I finish up some of my assignments)":
                    MC "(I’m bound to have some time sooner or later)"
            "Actually, if you’re that worried about me, how about cooking for me?":
                    show tsm ndeflecting
                    TSM "“No way, I have a life y’know?“"
                    MC "“You’re not gonna share your lunch with me?“"
                    show tsm nsmirk
                    TSM "“As if!“"
                    MC "“I thought so.“"
    
    scene campus1d with fade
    show tsm nnormal
    TSM "“Well, we’ve reached campus.“"
    MC "“Thanks for walking with me, it was nice seeing you again.“"
    show tsm nangy
    TSM "“Don’t get sappy.“"
    show tsm nsmirk
    TSM "{size=-7} “But well, I guess it was kinda nice.“ {/size}"
    MC "See you... some other time then?“"
    show tsm nhappy
    TSM "“See ya’“"
    hide tsm
    "With that, he turned his back and headed off to his building with a hand waved towards me."
    MC "(Guess I won’t be seeing him again for awhile.)"
    MC "(Time to go to my building, before I’m actually late)"
    
    scene class with fade
    "As I walk into class, I quickly pull my phone out of my pocket so I can check the time."
    "MC (Good thing I made it on time.)"
    "In the distance I see my friend wave at me while pointing at the seat next to theirs, they swiftly remove their backpack from the table as I approach them."
    MC "(Good thing they saved a seat for me.)"
    MC "“Thanks.“"
    F "“Any time.“"
    MC "“I’m not late am I?“"
    F "“Not yet, they haven’t even turned on the projector.“"
    F "“Did you finish Thursday’s assignment?“"
   
    menu:
                "Almost, I should be done by today":
                    F "“Good for you, I haven't even started.“"
                "Nope, I got a lot of catching up":
                    F "“Same here, it’s insane how much work they give us.“"
    
    MC "“Goodluck to both of us then.“"
    MC "“By the way, please wake me up if I fall asleep later. I’m trying to pay attention for once.“"
    F "“Sure thing, although I’m pretty sure you’re the only one paying attention in this class.“"
    F "“Like, look back there, you just know those two are playing games.“"
    F "“And that person over there is online shopping on their laptop.“"
    MC "“Well I’m trying not to do that for now.“"
    F "“For now.“"
    P "“All right, everyone sit down.“"
    MC "(And so it begins.)"
    
    scene class with fade
    F "“[MC]? You awake? Class is over.“"
    MC "“I am, I’m just a little sleepy.“"
    F "“Same here, I'm gonna go back and take a nap.“"
    F "“Are you gonna walk back?“"
    MC "“Yea, I’m trying to save up. Might as well get some exercise while I'm at it.“"
    F "“Well, see you tomorrow then! Stay safe!“"
    MC "“Thanks, see you tomorrow!“"
    MC "(Time to walk back so I can finish up that assignment)"
    
    scene campusd with fade 
    MC "(Maybe I should drop by the cafeteria so I can buy lunch?)"
    MC "(Yea, that sounds good. I’d rather not starve.)"
    "Before I could even lift my foot towards the cafeteria, my phone started ringing."
    MC "(Who is it?)"
    show phone nix
    "(Ah, it’s Nix.)"
    MC "(Nix was a friend I made back when I first got into college, apparently we went to the same highschool.)"
    MC "(Never met him before though, and none of my friends seemed to know anyone who matched my description of him.)"
    MC "(Still, he lives across from me and he’s been super nice ever since we met.)"
    MC "(Our schedules seem to match pretty well so I usually meet up with him at some point during my day.)"
    YM "[MC]! Are you heading back? Have you had lunch? I’m at the cafeteria right now, do you want anything? "
    MC "(I’m starting to think that Nix is psychic or something, his timing’s always been ridiculously good.)"
    MC "“Actually, I was just heading there. I was about to buy food before I headed back.“"
    YM "“What a coincidence, so am I! Want me to buy you some fried rice? I’m about to order mine so I might as well order one for you too.“"
        
    menu: 
        "Sure, thanks a lot":
                YM "“No problem.“"
                scene cafeteria with fade
                MC "(Where is he?)"
                show ym nhappy
                YM "“[MC]! I’m over here!“"
                show ym nsmile
                MC "“Thanks for ordering it for me, how much do I owe you?“"
                show ym nrhappy
                YM "“You don’t need to pay me back. After all, we’re friends right?“"
                show ym nsmile
                MC "“I should’ve known you wouldn’t let me pay you back.“"
                MC "“But you can’t keep doing this, I need to pay you back eventually. Who knows how many of my meals you’ve paid for by this point?“"
                show ym nhappy
                YM "“Just you being friends with me is enough.“"
                MC "“If you say so. Although one these days I’m gonna run up to you and slap a big envelope of cash right in your hands, and I’ll run before you can give it back.“"
                show ym nrhappy
                YM "“Sure, sure.“"
                show ym nsmile
                MC "“Anyway, let’s sit down.“"
        "Nah, I’ll eat something else today":
                YM  "“Okay, I'll wait for you so we can eat together.“"
                scene cafeteria with fade
                MC "(I think I’ll buy something from that stall today)"
                show ym nhappy
                YM "“[MC]! You’re here! Mind if I talk to you while you wait in line?“"
                MC "“Not at all, you talking to me would definitely keep my boredom away.“"
                show ym nrhappy
                YM "“I’m glad to be of service.“"
                YM "“How’s your day been [MC]?“"
                show ym nsmile
                MC "“Same old, same old. You?“"
                show ym nhappy
                YM "“I’ve been fine so far, and now that you’re here, it can’t be better.“"
                MC "“Stupid, you see me almost everyday.“"
                show ym nquestioning
                YM "“So?“"
                YM "“Is there anything wrong with enjoying the presence of a friend?“"
                MC "“Don’t you have other friends?“"
                show ym napologetic
                YM "“I do, but I like you the most.“"
                show ym nsmile
                LL "“Excuse me, what would you like?“"
                MC "“Oh sorry. Let’s see... I’ll take the...“"
    
    scene cafeteria with fade
    MC "“Alright, time to eat!“"
    MC "“Ooh, this is pretty good. I might order this again tomorrow.“"
    show ym nhappy
    YM "“I’m glad you like it.“"
    show ym nsmile
    MC "“What about you? D’ya like it?“"
    show ym napologetic
    YM "“Well I wouldn’t’ve ordered it if I didn’t like it.“"
    show ym nsmile
    MC "“Fair.“"
    show ym nhappy
    YM "“You don’t have anYMore classes after this, right, [MC]?“"
    show ym nsmile
    MC "“Nope, I’m ready to go back after we eat lunch.“"
    show ym nrhappy
    YM "“Nice, wanna walk back together?“"
    MC "“Sure. Why not?“"
    
    scene roadd with fade
    show ym nquestioning
    YM "“[MC], you sure you’re okay? You seem tired.“"
    MC "“Is something off about me? This is the second time I've been told that.“"
    show ym nnormal
    YM "“Who did?“"
    show ym nsilent
    MC "“My downstairs neighbor, I met him this morning. I haven’t seen him for a while.“"
    MC "“He also said  I seemed tired.“"
    show ym napologetic
    YM "“Maybe you’ve been a bit stressed out? You know you can count on me if you need anything.“"
    MC "“Nah, I’ll be fine, probably.“"
    show ym nhappy
    YM "“Or I can cook for you? Less time on worrying about what to eat means more time for something else, right?“"
    MC "“Since when do you cook“?"
    show ym nrhappy
    YM "“Starting now if you’d like.“"
    show ym nsmile
    MC "“Ha ha, no thanks.“"
    MC "“I’ve been managing just fine so far, you can worry about yourself first. Haven’t you been busy recently?“"
    show ym nhappy
    YM "“Yea well, I can always clear up time.“"
    MC "“No need, besides...“"
    
    scene kosd with fade
    show ym nsmile
    MC "“We’re already here!“"
    MC "“See you tomorrow? If we even see each other?“"
    show ym napologetic
    YM "“We always do though, one way or another.“"
    show ym nrhappy
    YM "“Well, see you tomorrow!“"
    MC "“Byee!“"
    hide ym
    MC "(Now that I'm back, it’s time to lock in and get things done.)"
    
    scene insidepr with fade
    MC "(Yikes, I forgot how messy my room is. Should I clean up now? I feel like i’ve been putting it off for some time.)"
    MC "(How much work do I have left? If I finish then maybe I’ll clean up some other time when I’m less busy.)"
    MC "(Yea, that sounds good.)"
    
    scene cg1 with fade
    MC "“Lock in [MC], you can do this.“"
    scene cg1 with fade
    MC "“Alright, done with that one. Now we can move on to...“"
    scene cg1 with fade
    MC "“This is due next week but if I start now...“"
    scene cg1 with fade
    MC "“Just a little more...“"
    scene cg1 with fade
    MC "“Am I..done?“"
    MC "“Let’s check one last time, no mistakes right?“"
    MC "(This part is fine, and this part...’s all good.)"
    MC "(I think I’m officially done!)"
    MC "(Thank...{size=-10} God, I can rest {/size})"
    scene black with fade
    "..."
    scene insidedream with fade
    GTWU "[MC]?"
    MC "(Huh? Who is it?)"
    menu: 
        "He sounds a little rough around the edges. I feel like I know him":
                $ TSM_route +=1
                GTWU "“If ya don’t wake up now, you're gonna be late.“"
                GTWU "“Geez, get an alarm or somethin’“"
                MC "“My bad.“"
        "Whoever it is, he’s friendly and chipper. He seems very familiar to me": 
                $ YM_route +=1
                GTWU "“Wakey wakey! It’s almost time for you to go!“"
                GTWU "“Please? [MC], won’t you wake up for me?“"
                MC "“Alright I’m up.“"
    
    "When I opened my eyes, I saw a boy in a cute maid outfit. I can’t quite make out any other discerning features about him but i’ve decided not to question anything."
    MC "(Who is this?)"
    
    menu: 
        "He looks pretty grumpy for someone in such a frilly apron, although the way his cheeks reddened is pretty cute.": 
                $ TSM_route +=1
                GTWU "“What’re ya lookin’ at? I said you’re gonna be late.“"
        "He seems pretty happy in the maid outfit, he keeps twirling around like there’s no shame in it.": 
                $ YM_route +=1
                GTWU "“Do I look cute? I thought the extra bows might make you happy.“"
    
    MC "(He’s cute.)"
    "He holds out a hand towards me and I grab it to steady myself out of bed, he seemed used to this."
    menu: 
        "He held out a lunch box towards me and quietly pointed at the table where breakfast had already been made. ":
                $ TSM_route +=1
                GTWU "“Uh, there’s breakfast. I made your usual.“"
                GTWU "“And here’s your lunch. Make sure you eat it, don’t skip meals.“"
                MC "“Don’t worry I won’t, thanks by the way.“"
        "He happily stood aside and made a gesture towards the floor and walls. It seemed like he cleaned it before I woke up.":
                $ YM_route +=1
                GTWU "“[MC], look! I swept and mopped the floors this morning. Did I do a good job?“"
                GTWU "“Oh! And I made breakfast, I hope you’re fine with your usual.“"
                MC "“I am, thanks a lot.“"
    
    MC "(Oh this is bliss, if only everyday can be like this.)"
    MC "(This is so nice, I don’t want to go back to what life was like before.)"
    MC "(Before? What happened before?)"
    MC "(Was my life not like this?)"
    MC "(Huh?)"
    
    if TSM_route >= 2:
        MC "(Actually, now that I think about it... That maid kinda reminds me of Rudy.)"
        MC "(I guess I do find him kinda cute.)"
        play sound "audio/alarm.mp3"
        scene cg1 with vpunch
        MC "(Shit, I must've fallen asleep at my desk)"
        MC "(My back hurts..)"
        GTWU "“Wait, please let me stay here!“"
        MC "(What’s going on?)"
        GTWU "“No please! I’ll pay up by the end of the week.“"
        MC "(...)"
        GTWU "“What do you mean you promised the room to someone else? They move in in 2 days?!“"
        MC "(Is that Rudy?)"
        
        scene hallwayd with fade
        show tsm nangry
        TSM "“I can’t find another place so quickly!“"
        MC "(Is he being kicked out???)"
        show tsm nsilent at left
        show ll normal at right
        LL "“I’m sorry, but you’ve been behind on paYMent for a while now.“"
        show tsm nnormal
        TSM "“Couldn’t you have at least warned me before doing this?“"
        LL "“Sorry, but if it helps, they move out next month? You can move back in then.“"
        show tsm nangry
        TSM "“Next month?! Where am I gonna live for this month then??“"
        show tsm serious
        LL "“Again, I'm sorry to hear that. But you’ll have to move out by tomorrow.“"
        hide ll normal
        show tsm nsdangry at center
        TSM "“Shit.“"
        show tsm nserious
        
        MC "(Should I.. .Not have seen that?)"
        show tsm nsdangry
        TSM "“Fuck are you doing here?“"
        show tsm nserious
        MC "“Sorry, I heard you shouting from upstairs and I got worried.“"
        MC "“Is there any way I can help?“"
        show tsm nsdangry
        TSM "“Nah, you can fuck off. It’s not your business, leave me alone.“"
        MC "(Ouch.)"
        show tsm nnormal
        TSM "“Why are you still here? If ya can’t help, then scram.“"
        TSM "“It’s not like you can do anything in this situation.“"
        show tsm nserious
        MC "(Wait a minute this could be the solution to all my problems (in a way).)"
        MC "(He needs a temporary place to stay doesn’t he? I can provide that.)"
        MC "(And he’s really good at cooking and housework... Something I'm less great at.)"
        MC "(I have a potentially devious idea thanks to my perfectly timed dream.)"
        show tsm nuhsure
        TSM "“What’s with that look on your face? Don’t tell me you’re gonna keep bothering me.“"
        MC "“Actually, I have an offer to make.“"
        show tsm nhuh
        TSM "“Huh?“"
        show tsm nsilent
        MC "“You’re good at cooking and cleaning and all that jazz, yea?“"
        show tsm nnormal
        TSM "“I’m not a moron, so yea.“"
        show tsm nsilent
        MC "“No need to diss me. Anyway, I happen to want someone to do all that stuff for me.“"
        MC "“And in exchange, you can stay with me for the month.“"
        MC "“For the low-low price of doing housework and wearing a maid outfit, you can live a month rent free at my place! I’ll also split the costs of whatever groceries you buy.“"
        MC "(Woops, the maid outfit portion slipped out.)"
        show tsm nbdeflecting
        TSM "“Maid outfit?? Staying with you?? Are you joking?“"
        MC "(For a moment I thought he’d be angrier at it, but his outburst comes off as huffy and embarrassed, maybe I can push further on this?)"
        MC "Not at all, I'm completely serious. "
        TSM "Why??"
        menu : 
            "Because you’d look cute in one and it could motivate me to finish my assignments?":
                show tsm nbsurprised
                TSM "!!!"
                "He proceeds to make the most undignified embarrassed squeak I've ever heard in my life,  seemingly flustered from what I just said."
                "Once he stopped making noises, he glanced at me before looking away and pouting."
            "Why not? Don’t you need a place to stay? I’m pretty sure every other place around costs double this one.":
                show tsm nsdquestioning
                TSM "“Yea... well... I guess...You’re not wrong.“"
                TSM "“Is the maid outfit really necessary though?“"
                MC "“Of course it is.“"
                show tsm npout
                "I give him my best assuring smile while he grumbles and looks away from me, seemingly unsure with my proposal. After some time he finally looks back at me, the redness yet to disappear from his cheeks."
    
        show tsm nbangy
        TSM "“Fine, I'll do it. But you better not get any weird ideas about this.“"
        MC "(WOO!)"
        show tsm npout
        MC "“I assure you I have no such thoughts.“"
        show tsm nsmirk
        TSM "“I have a hard time believing that.“"
        show tsm nquestioning
        TSM "“But...are you sure about this?“"
        MC "“Of course I am, I wouldn't have made the offer otherwise.“"
        show tsm nsdquestioning
        TSM "“You don’t have a significant other who’d be really mad at me for staying with you right?“"
        MC "“Nope?“"
        show tsm nuhsure
        TSM "“Are you sure?“"
        MC "“Hey, I think I'd know if I have someone.“"
        show tsm nnormal
        TSM "“Alright then, that’s something.“"
        show tsm nhappy
        TSM "“If you really don’t mind, I guess I'll do it.“"
        MC "“I’m glad you agreed, is it safe to assume you’ll move in tomorrow?“"
        TSM "“Yea...“"
        MC "“Okay then, I’ll clear up my place a bit.“"
        show tsm nsmirk
        TSM "“I’m starting to worry about what your place looks like now.“"
        show tsm nuhsure
        TSM "“Considering you want a maid to help clean, is it that bad now..?“"
        MC "“Oh come on, you’ve been in my room.“"
        MC "“It’s not {I}that {/I} bad.“"
        show tsm nsmirk
        TSM "“I sure hope it isn’t.“"
        show tsm nsilent
        "He pauses for a moment before looking like he just had a horrible realization, he immediately stares right into my eyes with a vaguely horrified look."
        show tsm nangy
        TSM "“You’re not giving me some skimpy dress are you?“"
        MC "“We’ll see about that.“"
        show tsm nbangy
        TSM "“And don’t you dare tell anyone about this arrangement.“"
        MC "“I don’t know~“"
        show tsm nbangry
        TSM "“If you keep messing around I’ll...I’ll-“"
        MC "“Relax, I won't.“"
        show tsm nsdnormal
        TSM "“Good, you better not.“"
        "He gives me a small smile as he heads back to his room on the bottom floor. When he reaches his door, he looks back at me, seeming a little surprised that I'm still here."
        show tsm nhappy
        TSM "“Thanks...[MC].“"
        MC "“No problem!“"
        hide tsm
        "And with that, he shuts his door and the silence of the night fills the halls."
        MC "(Well, I guess it’s time for me to buy a maid outfit.)"
    
    else:
        "(Actually, now that I think about it, that maid kinda reminds me of Nix.)"
        "(Do I like him now??)"
        play sound "audio/alarm.mp3"
        scene cg1 with vpunch    
        MC "(Fuck, I fell asleep on my desk.)"
        MC "(Tha was a bad idea.)"   
        GTWU "“CALL THE FIRE DEPARTMENT!!“"
        MC "(!!)"
        MC "(What was that ?? The fire department??)"
        GTWU "“GET SOME BUCKETS!“"
        MC "(Shit, I gotta get outta here.)"
        
        scene kosn with fade
        "When I finally went outside, all the other tenants were already there, helping the neighbors by carrying buckets of water."
        MC "(Is the building across mine ON FIRE???)"
        MC "(Wait, that’s where Nix lives!)"
        MC "(Is he okay? Where is he??)"
        "My eyes scan amongst the sea of people, hoping to see even a glimpse of his white hair running about. I rush about the crowd, trying to stay as calm as possible."
        MC "(He’s not inside the building, is he? I sure hope he’s okay.)"
        GTWU "“Everyone! Do we have more water?“"
        show ym nsilent
        MC "(!!)"
        MC "(It’s him!!)"
        show ym nsilent at left with move
        "As soon as I heard the voice I turned my head around to the source, to my delight it really was Nix!"
        show ym nsilent at right with move
        "He’s running about through the crowd carrying an empty bucket and as soon as he hands it over to someone else, another bucket filled with water is placed right in his hands causing him to rush back to the source of the fire."
        show ym nsilent at left with move
        MC "(I knew he was nice but I never quite expected him to be heroic like this.)"
        hide ym
        "(Wait, I should be doing that too!)"
        "I swiftly rush near the line of people passing buckets to each other, offering my help."
        "Not long after, it seems the fire has died down. Despite the intensity of the night, I'm just glad it didn’t seem like the building sustained any major damages."
        
        show ym nhuffy
        YM "“[MC]! There you are! Are you okay?“"
        MC "“I should be asking you that, what happened?“"
        show ym nworry
        YM "“I’m not sure, a fire broke out in one of the lower rooms.“"
        YM "“I haven’t checked yet but I don't think my room caught fire, or at least I hope not.“"
        show ym napologetic
        YM "“I feel like we managed to put out the fire before it breached the other floors,  the damage shouldn’t be too severe, I think.“"
        MC "“You think? That’s not very reassuring.“"
        show ym nworry
        YM "“I know...“"
        YM "“[MC], sorry but can I do something for a bit? Just for one minute, please?“"
        MC "“Okay?“"
        show ym nsmile:
           parallel:
               ease .5 zoom 1.75
           parallel:
               yalign 0.0
               linear 0.0 yalign 0.0 xalign 0.5
        "After hearing my okay, he gives me a little smile before he rests his head on my shoulders. I can’t tell if he’s crying or not, but I decided not to intervene in his little moment."
        show ym nworry
        "A few moments of silence pass between us before his hands start to wander and they grip the sleeve of my night wear, trembling slightly."
        "It’s almost surreal how he’s acting right now, he’s usually so...cheerful. I can feel my heart forming cracks at the edges, threatening to break completely at the sight of him like this."
        YM "“[MC]..I’m scared.“"
        show ym nwhine
        YM "“Do you think... I'm gonna be okay living there? What if another fire breaks out in my room?“"
        menu:
            "I ..don’t know.":
                    MC "(I’d rather not speak on things I’m unsure about, I can’t guarantee there won’t be another fire.)"
            "I’m sure you’ll be fine.":
                    MC "(If he’s worried right now the least I can give him is some comfort, right?)"
        
        YM "“I just..feel scared now. Like my knees are about to give up on me anytime soon.“"
        MC "“You were doing a great job helping put out the fire earlier?“"
        show ym nworry
        YM "“I’m glad you think so but...“"
        YM "“[MC]. I don’t feel safe in there anymore, can I.. live with you instead?“"
        MC "“Huh? Why?“"
        show ym nwhine
        YM "“I don't think I can stay there for much longer, I just get reminded of all the smoke and fire that I saw. Besides, I'm sure they need to do some repairs.“"
        YM "“Please [MC], at least just for a month? Let me stay with you...“"
        show ym nrhappy
        YM "“I can help you with whatever housework you have? I can cook for you!“"
        MC "“Are you sure about this?“"
        show ym nsmile
        "Seeing me inquire more about his request must’ve made him feel a glimmer of hope that I might agree, because his eyes lit up immediately at my words."
        show ym nhappy
        YM "“Yes! I’m really sure. I’ll do anything so I can stay with you!“"
        show ym nsmile
        MC "“Even if I make you walk around in a maid outfit?“"
        MC "(I should not have said that, I guess that dream I had is influencing me.)"
        show ym nnormal
        YM "“You want me in a maid outfit?“"
        menu: 
            "I’m just kidding, you don’t have to if it makes you uncomfortable?":
                    show ym nrhappy
                    YM "“No, I'll do it!“"
                    YM "“I’ll be the cutest maid you’ll ever see.“"
                    MC "(I was NOT expecting that.)"
            "Of course I do, who wouldn’t want a cute maid around?":
                    show ym nbsqueal
                    "He makes a noise that I could only describe as a combination of a strangled critter and high pitched squeak."
                    show ym  nhappy
                    YM "“You think I'm...cute?“"

        show ym nsmile
        MC "“Well, I do have one thing to say before we make the arrangement.“"
        show ym nquestioning
        YM "“What is it?“"
        MC "“Do you have another place to stay tonight? I’ll have to clear up my place for you to stay.“"
        show ym nhappy
        YM "“Now that you’ve agreed to house me for a month, I think I'll be fine just booking a hotel room for tonight...“"
        MC "“Are you sure? You didn’t look so well earlier, you okay alone?“"
        show ym nrhappy
        YM "“I’m sure, I feel better thanks to you.“"
        show ym napologetic
        YM "“Besides, I'll have to pack up my things, won't I?“"
        MC "“Well, if you say so.“"
        MC "“Just give me a call if you need me, okay?“"
        show ym nrhappy
        YM "“I will!“"
        
        hide ym
        "And with that, he skips back over to the entrance of the slightly charred building, carefully looking around, presumably looking to grab a few of his things. By this point the crowds have dissipated, residents of my place have returned to their rooms while others went off somewhere else, perhaps a friend's place."
        "After one final wave, he disappears inside."
        MC "(Well, I guess I’ll be having a roommate starting tomorrow.)"
        
        scene class with fade
        MC "(I could barely sleep last night. Maybe that’s the wrong word, it’s more like I chose to stay up.)"
        MC "(Between my sudden impulse decision to house a man and me rushing to make the place look ‘presentable’, I ended up barely sleeping.)"
        F "“You okay? You... almost look worse than yesterday.“"
        F "“Worse as in, you got less sleep.“"
        MC "“Oh man, is it that obvious? I guess a lot happened yesterday.“"
        F "“Unfortunately, but I guess you do look happier? Did you finish the assignment?“"
        MC "“I did! I have time for other things now.“"
        F "“Not if we get another assignment today.“"
        MC "“Ugh, don’t remind me.“"
        F "“Do you still want me to wake you up later?“"
        menu:
            "Nah, we sat back here for a reason.":
                    F "“Fair point.“"
            "Please do, my eyes are threatening to close any time soon.":
                    F "“Alright then.“"

label day1:   
    #TSM Maid day1
    if TSM_route >= 2: 
        scene inside with fade
        MC "(Time for some last minute preparations!)"
        MC "(Do I have an extra blanket for him? Oh yea I do.)"
        MC "(Anndd, this cupboard should be enough for his things, or at least I hope they are.)"
        "I check the notification on my phone, it’s Rudy saying he’ll come up to my room to start moving his stuff in a bit."
        MC "(I’m just glad he doesn’t have a lot of stuff, it was already a hassle trying to find a place for all of mine.)"
        MC "(I cleared up some room for him by shoving my stuff into the closet, hopefully it’s enough.)"
        MC "(The maid outfit I ordered also arrived this morning in one piece, i’m so glad instant delivery exists!)"
        MC "(I ended up going with the long skirt and apron for him, I sure hope it fits!)"
        play sound "audio/knock.mp3"
        MC "“Coming!“"
        "When I opened the other, I came face to face with Rudy who’s carrying a huge box in his hands. His shoulders and arms are also occupied by bags that are filled with a variety of things, ranging from blankets, books, cooking utensils to what I can only assume is a portable stove."
        show tsm nuhsure
        TSM "“Uh, hi?“"
        show tsm nsilent
        MC "“Hey, come on in! You can put your stuff over there.“"
        show tsm nnormal
        TSM "“Okay.“"
        scene inside with fade
        MC "“Do you think all your stuff would fit there? I can try clearing more room if it isn’t.“"
        show tsm nnormal
        TSM "“I think it should be enough. I don’t have a lot of stuff.“"
        show tsm nsilent
        MC "“Need me to help bring your other stuff up here?“"
        show tsm nnormal
        TSM "“Nah, this is it.“"
        MC "(Legit? That’s barely anything.)"
        show tsm nuhsure
        TSM "“Are you sure you’re cool with me here?“"
        MC "“Of course I am.“"
        show tsm nsdquestioning
        TSM "“Ookay...Just making sure.“"
        show tsm nsilent
        "He turns his attention away from me and onto his belongings as his arms swiftly start unloading items from the giant box and all the bags."
        show tsm nuhsure
        TSM "“I put this here, right?“"
        show tsm nsilent
        MC "“Yep.“"
        "He nods and gives me a short hum in response as he continues to silently unpack his things. Not wanting to bask in awkward silence, I decided to at least attempt some small talk with him."
        MC "“So, got any questions about our arrangement?“"
        show tsm nnormal
        TSM "“Let me think...“"
        TSM "“Hmm...“"
        show tsm nsilent
        "He ponders the question for a bit as the contents of the box quickly dwindle down to nothing, eventually his hands make a sharp halt and all his movements pause as if trapped in time."
        show tsm nsdquestioning
        "“Um...I feel like I should've asked yesterday but...where do I sleep? I’m not...not... Y’know...“"
        MC "“Not what?“"
        show tsm nsdbangy
        TSM "“Are you really gonna make me say it?“"
        show tsm npout
        MC "“Well if you don’t use your words I won’t get you.“"
        show tsm sdbangy
        TSM "“Urgh.“"
        show tsm nsdquestioning
        TSM "“I...I’m not sleeping with you right? There’s only one bed.“"
        menu:
            "You’re not? I even prepared space on my bed for you.":
                    show tsm nbdeflecting
                    "He stares at me, mouth agape as if he can’t believe the obscenity that came out of my mouth."
                    TSM "“You can’t be serious...!“"
                    show tsm nbsurprised
                    MC "“What if I am, hmm?“"
                    MC "({I}Oh{/I} , tormenting him like this is fun.)"
                    "I step closer to him, positioning our faces mere inches from each other as he backs away from me, slowly backing himself up against the door."
                    show tsm nsdbangy
                    TSM "“Stop messing with me...“"
                    MC "“What if I'm not?“"
                    show tsm nbsurprised
                    TSM "“Hngh...!“"
                    MC "(Maybe this is enough teasing, he seems like he might run out my room already and he hasn’t even been in here for 5 minutes.)"
                    MC "“I’m sorry, you don’t have to if you don’t want to. I’m just teasing.“"
                    show tsm nbangy
                    TSM "“You..!.“"
                    show tsm nsdquestioning
                    "He breathes a sigh of relief but his eyes are mixed with a tinge of disappointment."
                    show tsm nsdnormal
                    TSM "“Well, good.“"
            "Of course not, I like my space.":
                    show tsm nhappy
                    TSM "“That’s good.“"
        show tsm nsilent
        MC "“I have a mattress for you to sleep on? Would that be fine with you?“"
        show tsm nhappy
        TSM "“Yea.“"
        show tsm nsilent
        MC "“Anything else you wanna ask?“"
        show tsm nunsure
        TSM "“Umm, you mentioned housework, yea?“"
        MC "“Yep.“"
        TSM "“What exactly do you want me to do here?“"
        MC "“Well, you can sweep the floors once every few days?“"
        show tsm nhuh
        TSM "“Few days? Don’t you sweep it everyday?“"
        MC "“Umm, no?“"
        show tsm nnormal
        TSM "“I’m not standing for that. Now that this is my place too, I'll sweep everyday.“"
        show tsm nuhsure
        TSM "“How often do you clean the bathroom?“"
        show tsm nsilent
        MC "(Yikes, recently the answer has been ‘whenever I have time’. I have a feeling he’s not gonna like that answer.)"
        MC "“Once every 2 weeks?“"
        show tsm nnormal
        TSM "“I’ll do it once a week.“"
        show tsm nhappy
        TSM "“Also, I'm guessing you want me to cook? You usually start drooling whenever I bring out my lunch.“"
        menu:
            "I do not!":
                    show tsm nsmirk
                    TSM "“You totally do, stop lying.“"
                    TSM "“Is that a no then?“"
                    MC "“No, please do cook for me.“"
            "Not my fault your food looks good.":
                    show tsm nsmirk
                    TSM "“Is that a yes?“"
                    MC "“Totally.“"
        show tsm nsilent
        MC "“Actually, there’s something else that you forgot to mention.“"
        show tsm nuhsure
        TSM "“What, you want me to mop the place too? I can do that.“"
        show tsm nsilent
        MC "“Appreciated but not that!“"
        show tsm nhuh
        TSM "“Huh? What else?“"
        "My lips curve into an evil grin, sensing my sudden shift he tenses up like a grumpy cat who’s about to get hugged."
        show tsm nbangy
        TSM "“I have a feeling I’m not gonna like this.“"
        MC "“Don’t tell me you forgot the maid outfit?“"
        show tsm nsurprised
        TSM "(!!)"
        show tsm nsdbangy
        TSM "“Tch, I was hoping you’d forget.“"
        show tsm npout
        MC "“Absolutely not! This is the most important part of the deal!“"
        MC "“Here I have it ready for you! Try it on.“"
        show tsm ndeflecting
        TSM "“Why do you have a maid outfit ready just like that??! It’s not from an ex or something is it?“"
        show tsm npout
        MC "“There’s something called express shipping, I bought it last night.“"
        MC "“Now don’t be shy and try it on! I’ll need to return if it's not your size.“"
        show tsm nangy
        TSM "“Do I really have to?“"
        MC "“Yep, this is mandatory.“"
        show tsm nsdangy
        TSM "“Fine, give me the outfit.“"
        hide tsm
        "Begrudgingly, he takes the fit and all its accessories from my hands and heads towards the bathroom to change."
        MC "“Don’t forget the stockings!“"
        TSM "“Shut up!“"
        "After shuffling around the bathroom for a bit, out came the beautiful maid from my dreams."
        show tsm mbangy
        TSM "“I’ve put it on.“"
        show tsm mbpout
        "He fidgets with his hands nervously as my eyes are glued straight onto him, staring like he’s a delicious piece of steak. He tries to steal a glance to gauge my approval but quickly turns away."
        show tsm mbangy
        TSM "“So? Take a picture why don’tcha it’ll last longer.“"
        show tsm mbpout
        MC "“You look so cute!!“"
        show tsm mbdeflecting
        TSM "“Huh? Cute?!“"
        show tsm mbsurprised
        MC "“I knew this was the right one for you.“"
        MC "“Can you give me a twirl?“"
        show tsm mangy
        TSM "“I am NOT twirling for you!“"
        show tsm mbpout
        MC "“Shame, but I really do mean it. You look great.“"
        show tsm mbsdquestioning
        TSM "“Stop lying.“"
        MC "“I’m not...!“"
        show tsm mangy
        TSM "“You are! There’s no way something this frilly would look good on me!“"
        MC "“How ‘bout {b}you{/b} stop lying? You look GREAT!“"
        show tsm mdeflecting
        TSM "“Stop..!“"
        show tsm mstopit
        MC "“Stunning, gorgeous, beautiful.“"
        show tsm mangy
        TSM "“No..!“"
        MC "“Eye catching, Jaw dropping, head turning.“"
        show tsm mstopit
        TSM "“H-hey...!“"
        MC "“Absolutely adorable yet very elegant, the-“"
        show tsm mbstopit
        TSM "“‘Okay that’s enough!“"
        MC "(!)"
        play sound "audio/thud.mp3"
        show tsm mbsurprised:
           parallel:
               ease .5 zoom 2.0
           parallel:
               yalign 0.0
               linear 0.0 yalign 0.0 xalign 0.5
        "As he lunges towards me in an attempt to stop me from spouting words of praise, I lose my balance while trying to dodge and we both end up tumbling onto my bed."
        "I fell on top of him, bracing my hands against my bed so as to not crash right into him as he stared wide eyed at me, completely mortified about our current position."
        show tsm mbsdquestioning
        TSM "{size =-10}“shit...“{/size}"
        TSM "“Y-ya mind getting off?“"

        TSM "“Y...you’re kinda...y’know...“"
        menu : 
            "Sorry!":
                    "Quickly I got off of him, feeling a little bad that I flustered him to this degree."
            "I mind":
                    show tsm mbsurprised
                    "I give him a mischievous grin as I pin him further into the mattress, he looks away from me, desperately trying to hide his face in the sheets."
                    "Unfortunately for him, our current position doesn’t quite give him the range to do it so he ends up merely looking to the side, his expression still fully exposed to me."
                    show tsm mbsdquestioning
                    TSM "“W-what? Don’t look at me like that.“"
                    show tsm mbangy
                    TSM "“Just...get off already!“"
                    show tsm mbpout
                    MC "“What if I don’t want to?“"
                    MC "“Actually, here’s a deal. I’ll get off once you admit that you’re cute!“"
                    show tsm deflecting
                    TSM "“That’s not fair!“"
                    MC "“It is though, just 2 words and you’re free.“"
                    show tsm mbstopit
                    TSM "“You...!“"
                    show tsm mbpout
                    MC "“Just two words“."
                    show tsm mbangy
                    TSM "“Fine, I-I’m c-cute.“"
                    MC "“There we go! Good boy.“"
                    show tsm mbsurprised
                    TSM "(!)"
                    "Finally, I stood up from our position, freeing him from my temporary prison."
    
        hide tsm
        MC "(I think that’s enough excitement for today, I should stop now.)"
        MC "(I’ll just continue on with my assignments.)"
        
        scene insided with fade
        show tsm suhsure
        TSM "“Hey, um aren’t you gonna sleep?“"
        show tsm ssilent
        MC "“Huh?“"
        show tsm snormal
        TSM "“It’s getting late, and well, I’m gonna sleep.“"
        show tsm ssilent
        MC "(Oh shit, what time is it?)"
        "I glance at the clock only to find out that he was right, it is getting late.“"
        MC "“Sorry, i’ll quiet down. Do you want to turn the lights off?“"
        show tsm suhsure
        TSM "“Aren’t you still busy? Working in the dark hurts your eyes, y’know?“"
        MC "“I know, but isn’t it hard to fall asleep with the lights on?“"
        show tsm shappy
        TSM "“s’fine, worry about yourself first...“"
        show tsm ssilent
        MC "(Man, he’s actually really nice. I’m starting to feel bad for potentially disturbing his sleep, maybe i’ll sleep in a bit. Just after I finish this one part.)"
        MC "“Okay then, Goodnight Rudy.“"
        show tsm shappy
        TSM "“Yea, g’night...“"
        
        scene insiden with fade
        MC "(Alright, we’re done with the whole thing! I’ll be completely free tomorrow.)"
        MC "(I know I said ‘just this one part’ but that’s always a lie.)"
        MC "(Whatever, Time to sleep!)"
        "I look down at the mattress on the floor where Rudy is seemingly fast asleep, I’m glad I wasn’t inhibiting his sleep too much."
        MC "(Oh well, goodnight world.)"
        jump day2_tsm
    
    
    else:
    #YM Maid day 1
        scene inside with fade
        MC "(Is everything ready? I hope I have an extra blanket for him.)"
        MC "(He seemed so startled yesterday, i’m hoping I don’t make him too uncomfortable.)"
        MC "(Is this enough space for his things? I sure hope so.)"
        "I check my phone to see any news from Nix, he did say he’ll be arriving in a bit and he lives right across the street."
        MC "(I wonder when he’ll arrive.)"
        play sound "audio/knock.mp3"
        YM "“[MC], I’m here!“"
        MC "“Coming!“"
        show ym nsmile
        MC "“Heyy. You seem well, or at least better than yesterday.“"
        show ym nhappy
        YM "“How can I be scared if I'm staying with you?“"
        MC "“I don’t know, what if my place gets set on fire?“"
        show ym napologetic
        YM "“[MC]... Don’t joke around like that...“"
        show ym nsmile
        MC "“Sorry, come on in. You can put your stuff over there.“"
        scene inside with fade
        MC "“Need any help?“"
        show ym nrhappy
        YM "“Sure!Thanks a lot.“"
        show ym napologetic
        YM "“I’ll start by unpacking my clothes, where do I...?“"
        MC "“Over there, I moved my clothes so you can use the other half of my wardrobe.“"
        show ym nrhappy
        YM "“Okayy!“"
        show ym nsmile
        "He cheerfully skips around to my closet, and starts pulling out some shirts, carefully categorizing them in his mind."
        hide ym
        "While he does that, I'll just get his textbooks out of the box. That shouldn’t be too invasive for me to handle, right?"
        MC "(Ah, I have this textbook too, I should separate it from mine so I wouldn’t get mixed up)"
        "(What’s this one? I don’t think I have this class.)"
        MC "(It’s kinda interesting seeing the differences in our fields of study.)"
        show ym nrhappy
        YM "“[MC], I’m done!!“"
        MC "“That was quick.“"
        show ym nhappy
        YM "“Well, the sooner I finish unpacking, the sooner we can do something else right?“"
        show ym nquestioning
        YM "“Actually, I have a question.“"
        MC "“Ask away."
        show ym nhappy
        YM "“[MC]...There’s only one bed, are we sleeping together?“"
        menu:
            "Don’t worry, I've got a spare mattress.":
                    $ YM_dp +=1
                    show ym nnormal
                    YM "“Oh.“"
                    show ym nsilent
                    MC "“I have a spare blanket for you to use? I swear you won’t be cold at night.“"
                    show ym nhappy
                    YM "“Okay then, thanks.“"
            "I don’t know. Do you want to?":
                    show ym napologetic
                    YM "“Can I...really?“"
                    MC "(Oh shit, I was not expecting him to be this happy about it.)"
                    MC "(I was kinda joking, how do I defuse this?)"
                    MC "“Wouldn’t it be a bit cramped?“"
                    show ym nhappy
                    YM "“Not at all, your bed looks pretty big.“"
                    show ym nsmile
                    MC "(Damn it, does he actually wanna share a bed?)"
                    "(You know what? Screw it! I can use an extra stuffed animal.)"
                    MC "“I hope you don’t mind if I accidentally hug you when we sleep.“"
                    show ym nrhappy
                    YM "“That’s all good with me!“"
                    show ym nsmile
                    MC "“Or if I kick you off the bed.“"
                    MC "“Maybe we should have the mattress on the floor, just in case.“"
                    show ym nhappy
                    YM "“Okay, then!“"
        
        show ym nrhappy
        YM "“I swear you won’t regret agreeing to let me stay! I’ll clean and cook everyday for you!“"
        show ymsmile
        MC "(I feel like I should’ve realised this yesterday, but whatever the fuck he’s doing is starting to feel less than platonic to me.)"
        MC "(Does he like me or something? Even if he does, who the fuck goes this far for a simple crush?)"
        menu:
            "(I mean, I kinda like him too so this works out great)":
                    "(He’s pretty cute and I can’t think of any reason to not want to date him so far.)"
                    "(If he really is into me that is.)"
            "(Cool, I’m gonna ignore this and brush off everything he does as a platonic gesture.)":
                    "(Let’s not question anything, especially when this scenario helps with my ‘I don’t have time for housework’ problem.)"
        MC "“Don’t you have college too? Wouldn’t it be a bit much?“"
        show ym nhappy
        YM "“Not at all, I'll try my best.“"
        show ym nrhappy
        YM "“OOH! I almost forgot about this.“"
        MC "“What is it?“"
        show ym napologetic
        YM "“Can you close your eyes? It’ll be a surprise.“"
        show ym nsmile
        MC "“Okay?“"
        scene black with fade
        MC "“Alright, my eyes are closed.“"
        YM "“Wait just a sec, don’t peek okay?“"
        play sound "audio/fabric.mp3"
        "As soon as he said that, I heard the sound of fabric swishing around and dropping to the floor."
        MC "“What are you doing?“"
        YM "(!!)"
        YM "“[MC]! Please don’t look!“"
        MC "“I’m not! I just felt something fall near my foot. Are you changing..?“"
        YM "“Oh, sorry about that. Yes I am.“"
        YM "“Wait, just a bit more...“"
        "I hear him rustle about the place, opening the wardrobe and closing it before shuffling back near me."
        YM "“Okay, you can open your eyes now!“"

        scene inside with vpunch
        MC "“Is that??!“"
        show ym mrhappy
        YM "“Ta-da! Do you like it? I bought it last night!“"
        "Nix twirls around in the short skirt of his maid outfit, showing off every frill and ribbon that decorated it. "
        MC "(Holy shit, this is straight out of my dream!)"
        show ym mworry
        YM "“[MC]? Um...do you not like it?“"
        menu : 
            "Are you kidding? You look cute as hell!":
                    show ym mrhappy
                    YM "“[MC]! I’m glad you think so!“"
                    YM "“Here, you can take a closer look at the accessories too.“"
                    YM "“Am I the cutest maid you have?“"
                    MC "“Nix, aren’t you my only maid?“"
                    "Hearing that, he squeals in delight and hugs me tight, burying his face deep in my chest."
                    show ym msqueal:
                            parallel:
                                ease .5 zoom 2.0
                            parallel:
                                yalign 0.0
                                linear 0.0 yalign 0.0 xalign 0.5
                    YM "“I’m glad to hear that!“"
                    show tsm mbsurprised:
                            parallel:
                                ease .5 zoom 1.0
                            parallel:
                                yalign 0.0
                                linear 0.0 yalign 0.0 xalign 0.5
            "Why?":
                    $ YM_dp +=1
                    MC "“I mean you look cute but I definitely wasn’t expecting this.“"
                    show ym mquestioning
                    YM "“Oh, but you still think I look cute, right?“"
                    MC "(Oh no, there’s no way I can be mean to him when he’s like this)"
                    MC "“You do.“"
                    "He gives me a small grin in response, I hope that was enough of an answer for him."
    
        "Eventually, he lightly taps my shoulder and points to the bed as if he wants me to sit down. When I obliged, he sinks down and places his head on my lap then he carefully grabs my dominant hand and places it on his head."
        show ym mapologetic:
                              parallel:
                                   ease .5 zoom 1.5
                              parallel:
                                   yalign 0.0
                                   linear 0.0 yalign 0.0 xalign 0.5
        YM "“Come on, don’t you wanna pet me? My hair is soft.“"
        show ym msmile
        MC "“I feel like, {b}you{/b} are the one who wants to be pet.“"
        show ym mquestioning
        YM "“You don’t want to?“"
        show ym msmile
        MC "(Aww, look at him. I can’t refuse him when he’s like this.)"
        MC "“Alright, just for a few minutes though.“"
        show ym mcontent
        "I proceed to stroke his hair with light touches, I suppose this is the closest I've ever been to feeling like I have a pet in college."
        "As he kneels on the rug, he responds favorably  to my touch, almost like a cat purring when being petted by their owner."
        show ym mapologetic
        YM "“Thank you, [MC]... This is nice.“"
        YM "“I’m glad you agreed to let me stay.“"
        MC "“Hmm.“"
        show ym msmile
        
        menu: 
            "I think this is enough petting, no?":
                    $ YM_dp +=1
                    show ys mtch
                    YM "{size=-10}“tch “{/size}"
                    show ym mhappy
                    YM "“Okayy, how was it? I’m soft, no?“"
                    show ym msmile
                    MC "“You are.“"
                    MC "“But I think it’s time we stop, I still have my assignments and I'm sure you have some studying to do as well.“"
                    show ym mnormal
                    YM "“Fine...“"
            "By this point you feel more like a pet than a roommate, don't cha think?":
                    show ym mquestioning
                    YM "“Is that what you want? Then, I can be that too. I can be both.“"
                    show ysm msmile
                    MC "({I}Oh?{/I})"
                    show ym mgrin
                    YM "“I’ll be your maid and your pet.“"
                    show ym mhappy
                    YM "“You like cat boys, don’t you?“"
                    MC "“Who doesn’t?“"
                    show ym mquestioning
                    YM "“I don’t know, some people might prefer other animals.“"
                    show ym msmile
                    MC "“I guess.“"
                    MC "“You are pretty cute like this though.“"
                    show ym mcontent
                    "He buries his face even further into my lap and lets out a muffled noise that I can't quite make out."
                    MC "“Although, as much as I like having you kneeled next to me like this, I have work to do.“"
                    MC "“I’m sure you have some studying to do, no?“"
                    show ym m worry
                    YM "“Can I study next to you while you work on your assignments?“"
                    MC "“Sure?“"
                    show ym mrhappy
                    YM "“Yay!“"
        
        MC "(I guess this is my life with Nix now, time to get back to work.)"
        hide ym

        scene inside with fade
        show ym squestioning
        YM "“Hey, [MC]?“"
        YM "“Aren’t you gonna sleep now? You’ve been working nonstop.“"
        show ym ssmile
        MC "“Huh?“"
        "I take a quick glance at my clock only to be met with the realization that it’s quite late at night."
        MC "(Damn, I guess I haven't been paying attention at the time.)"
        MC "“I’ll go to sleep in a bit, I just need to finish this one part first.“"
        MC "“If you’re going to sleep, I'll try to keep it quiet.“"
        show ym srhappy
        YM "“No it’s okay, it’s kinda soothing to know that you're near me.“"
        MC "“Okay then, Goodnight Nix.“"
        show ym shappy
        YM "“Good night [MC]...“"
        
        scene insiden with fade
        MC "(I know I said ‘Just this one part’, but I ended up doing more than expected.)"
        "I peek at Nix, sleeping peacefully while huddled up inside my spare blanket. He just looks so...cozy."
        MC "(I guess that settles it, I’m going to bed.)"
        MC "(Goodnight, world.)"
        scene black with fade
    
        if YM_dp == 3:
            "..."
            YM "“[MC]..I-i’m so close to you I can hardly breathe...“"
            YM"What do I n-need to do to make you love me? I tried my hardest today for you...“"
            YM "“D-don’t I look cute today, [MC]“?"
            YM "“Why do you not want me? P-please tell me...“"
            YM "(...)"
            YM "(I’ll keep trying tomorrow [MC], you will love me. There can’t be any other choice.)"
            jump day2_ym
        else:
            jump day2_ym

label day2_tsm:
    scene black with fade
    #TSM Maid day2 morning

    TSM "“Hey, uh, wake up.“"
    MC "(?)"
    TSM "“Ah shit, [player_gender] [player_sb] NOT waking up.“"
    TSM "“Hey, breakfast is done. It’ll be cold if you wait too long.“"
    TSM "..."
    TSM "“Shit, [player_gender] won’t wake up.“"
    TSM "“Uhh... Should I poke [player_object]?“"
    TSM "“Ugh...But [player_gender]’ll think I'm weird if I do this.“"
    TSM "“Wake up, [MC].“"
    TSM "{size=+5} “FUCK, I give up!“ {/size}"
    scene inside with vpunch
    MC "(!!!)"
    MC "“Huh? What happened?!“"
    show tsm nsdangy
    TSM "“N-nothin’ Breakfast is done.“"
    show tsm nsilent
    "Looking around my room, I noticed that it was miraculously shinier than before. Definitely Rudy’s doing."
    MC "“What got you yelling up so early?“"
    show tsm ndeflecting
    TSM "“It was nothing!“"
    MC "“Okay?“"
    menu: 
        "(I should go have breakfast)":
                MC "“Thanks for breakfast!“"
                show tsm nnormal
                TSM "“Don’t mention it.“"
                TSM "“I’ll be off now.“"
                MC "“This early? You got morning classes?“"
                TSM "“Nah, just wanted to go for a run.“"
                MC "“Okay then, byee!“"
                hide tsm
        "Are you sure though?":
                show tsm nangy
                TSM "“I said it was nothing.“"
                MC "“Really?“"
                show tsm nbdeflecting
                TSM "“Yes! Now go have breakfast, I’m going for a run!“"
                hide tsm
                play sound "audio/doorop.mp3"
                MC "(Woops, I must’ve scared him off.)"
                    
    scene campus1d with fade
    MC "(Man, having breakfast sure is great.)"
    MC "(Recently, I’ve been neglecting breakfast since I’ve been rushing. With Rudy around I finally have the time to sit down and eat properly.)"
    MC "(And the floor! Not a hair in sight!)"
    MC "(I mean I did sweep the floor before he got there but there’s always runaways here and there.)"
    MC "(Man, he’s only been here for one day and he’s already improved my life.)"
    MC "(I really gotta get my shit together before I have to fend for myself again.)"
    MC "(Oh? Is that Rudy?)"
    MC "(That’s rare, usually I never see him around campus. \)"
    MC "(Most of the time it’s Nix who I encounter. Maybe I should say hi while he’s there?)"
    MC "(But he’s with his friends, would it be alright if I intrude?)"
    menu : 
        "Go up to him.":
                MC "(To hell with it! He’s my friend and I can say ‘hi’ whenever I want, i’ll just leave immediately afterwards.)"
                show tsm nsurprised
                "As I approach, he freezes up on the spot, when his friends notice his reaction I can see the edges of their mouth curl up into a smile, with one nudging Rudy towards me."
                MC "“Hi! I don’t see you around campus much, whatcha up to?“"
                show tsm nnormal
                TSM "“Uh I’m just here to help fundraise for my club.“"
                show tsm nsilent
                MC "“Oh right, I almost forgot you were in the badminton club.“"
                show tsm nnormal
                TSM "“Yea, we’re raising money to rent a bus for our next tournament.“"
                show tsm nsilent
                show fs normal at right
                show ls normal at left
                FS "“You should try one of the crepe cakes he made, they’re super good!“"
                LS "“You NEED to know how good his food is!!“"
                MC "(Oh they’re REALLY excited about his cooking.)"
                FS "“Oh totally! We’d steal his lunch if we could.“"
                LS "“Any [player_sd] that dates him will sure be happy for the rest of [player_possessive] life!!“"
                MC "(If I didn’t know any better, I’d say they’re tryin’ to gas him up in front of a crush or something.)"
                MC "(But nope, it’s just me.)"
                MC "(Unless?)"
                MC "(Just kidding, probably not. Especially not after I almost killed him from sheer embarrassment with that maid outfit.)"
                FS "{size=-10}“Bro, go for it“{/size}"
                show tsm nsdangy
                TSM "“grr.“"
                show fs normal:
                        linear 0.050 xoffset -10
                        linear 0.050 xoffset +0
                        linear 0.050 yoffset -10
                        linear 0.050 yoffset +0
                        # repeat 2"
                show tsm nsilent
                FS "{size=-10} “What the fuck man? We’re tryin’ to help you here.“"
                LS "“Don’t you like [player_object]?“"
                show tsm ndeflecting
                TSM "“NOT ANOTHER WORD DUMBASS.“"
                show tsm nnormal
                TSM "“Sorry ‘bout that. Ignore them, their stupidity is contagious.“"
                MC "“It’s okay, I'll buy one. They’ve sold me on your skills.“"
                show tsm nsilent
                "The friendly looking one gives Rudy a cheerful thumbs up in response while the loud one nudges him lightly."
                show tsm nuhsure
                TSM "“Really?“"
                MC "“Yep!“"
                show tsm nhappy
                TSM "“Well then, thanks? Here’s the crepe cake.“"
                show tsm nhuh
                MC "“And here’s the money.“"
                MC "“Oh wait, here’s a tip!“"
                MC "“See you later!“"
                show tsm silent
                hide tsm
                hide ls
                hide fs
                FS "“{I}Ooooh ‘see you later~“{/I}"
                FS "“Ow! Quit it man, it worked didn’t it?“"
                "By this point I was on my way to my next class, but I have a feeling that guy got elbowed pretty badly again."
                MC "(Still, seeing Rudy flustered never fails to make me break out into a grin.)"

        "Awkwardly ponder your next move. (Incase you do anything stupid)":
                MC "(Shit, what do I do? Is it rude if I keep walking?)"
                "When the two people next to Rudy noticed me, they seemed to get a little excited."
                "That’s when I finally noticed the stack of cakes behind them, maybe they’re selling them to raise funds for something?"
                MC  "(I guess they’re excited to see a potential customer?)"
                "Eventually the person on the right lifts up Rudy’s entire right arm and makes him wave at me."
                MC "(Well, now it’d definitely be rude if I don’t wave back.)"
                "Seemingly flustered with what his friend made him do, he quickly turns to scold him."
                "I give him a small wave in return and politely excuse myself from the situation."
                MC "(That could’ve gone worse.)"
    
    show ym nquestioning with vpunch
    YM "“[MC]?“"
    show ym nsmile
    MC "(!)"
    MC "“Geez man, you spooked me. What’s up?“"
    show ym nhappy
    YM "“I saw you from afar and figured i’d talk to you. Our next class is in the same building, right?“"
    show ym nsmile
    MC "“Man, you know my schedule so well. {i}Too {/i} well actually.“"
    show ym nrhappy
    YM "“Of course I do! I'm your closest friend, right?“"
    show ym nsmile
    "For a moment, I hesitated. Is he?"
    MC "(I’m trying to think about it but for some reason Rudy pops up in my head instead.)"
    MC "(That’d be mean to outright say to Nix though.)"
    MC "“I don’t know, maybe?“"
    show ym nhuffy
    YM "“Boo! [MC]...“"
    show ym nsmile
    MC "“Sorry! Let’s go, shall we?“"
    show ym nhappy
    YM "“Sure.“"
    show ym nquestioning
    YM "“Who was that anyway? I’ve never seen you talk to him before.“"
    show ym nsilent
    MC "“Oh that’s my downstairs neighbor. Our schedules never align though so I barely see him.“"
    show ym nmnormal
    YM "“I see.“"
    
    
    scene class with fade
    MC "(WOO!! Class is OVER!)"
    MC "(And since I finished most of my assignments yesterday, I’m practically free tonight.)"
    F "“You seem pretty happy.“"
    MC "“Who wouldn’t be if they'll be practically free tonight?“"
    F "“You’re done with the assignments?“"
    MC "“Yup!“"
    F "“Damn lucky, I still have something after this.“"
    F "Well, see you tomorrow.“"
    MC "“Byee!“"
    play sound "audio/notifhp.mp3"
    MC "(Huh? Wonder who’s that from? Is it Nix?)"
    "(Well usually it is.)"
    show phone tsm
    "To my surprise, it's actually Rudy. Which is pretty unusual since the last time I texted him was to ask if the power at our place went down a few months ago."
    TSM "“What do you want for dinner?“"
    TSM "“I’m about to go shopping.“"
    MC "(What do I want to eat? Honestly not sure yet.)"
    MC "(Actually, here’s an idea...)"
    MC "“Why don’t I go with you? I can pick out the things I want there.“"
    TSM "“Ok, I’ll be at the supermarket in 10 minutes.“"
    MC "“Okayy, see you there!“"
    
    scene roade with fade
    show tsm nsilent
    MC "“Heyy! I’m here.“"
    "When I eventually spot him from the crowd, he already has a basket in hand. I guess I was late?"
    MC "“Did you wait long?“"
    show tsm nnormal
    TSM "“Nah. Let’s go“"
    
    scene supermarket with fade
    MC "“So where do we start?“"
    show tsm nnormal
    TSM "“I just follow the layout of the store.“"
    TSM "“We can start from here.“"
    show tsm nsilent
    "The first section we’ve reached is the produce section, I can see the almost unfamiliar view of all the fruits and vegetables that I barely consumed recently."
    jump veggies
    
label veggies:

    $ Spinach = False
    $ Carrots = False
    $ Apples = False
    $ Onions = False
    $ Tomato = False
    $ Oranges = False
    $ Thats = False

label choose_veggies:

    if Spinach and Carrots and Apples and Onions and Tomato and Oranges and Thats:
        jump TSMafterloop1

    menu:
        MC "“I think I'd like...“"

        "Spinach" if not Spinach:
            TSM "“Sure.“"
            $ Spinach = True
            jump choose_veggies

        "Carrots" if not Carrots:
            TSM "“Okay.“"
            $ Carrots = True
            jump choose_veggies

        "Apples" if not Apples:
            TSM "“Why not?“"
            $ Apples = True
            jump choose_veggies

        "Onions and Garlic" if not Onions:
            TSM "“Can't go wrong with those.“"
            $ Onions = True
            jump choose_veggies

        "Tomatoes" if not Tomato:
            TSM "“Okay.“"
            $ Tomato = True
            jump choose_veggies

        "Oranges" if not Oranges:
            TSM "“Alright.“"
            $ Oranges = True
            jump choose_veggies

        "That's All" if not Thats:
            $ Thats = True
            jump TSMafterloop1 

label TSMafterloop1:   
    MC "“Where to next?“"
    show tsm nnormal
    TSM "“Just straight ahead.“"
    show tsm nhappy
    TSM "“Want some rice? I’ve got a rice cooker.“"
    TSM "“How about the eggs?“"
    menu:
        "Just the rice is fine.":
            jump next
        "I’ll take the eggs, no rice though.":
            jump next
        "Both sound great!":
            jump next
        "Can we get some bread instead?":
            jump next
        "Nah, I think this is it.":
            jump next

label next:
    show tsm nsmirk
    TSM "“Cool, let’s head to the checkout now.“"
    show tsm nsilent
    "As the cashier scans our things, I catch her eyeing me and Rudy."
    MC "(Is something... Wrong? Hopefully that’s just my imagination.)"
    C "“Your total is this much, how would you like to pay?“"
    "Before Rudy can pull out his wallet, I go ahead and tell her to give me the QR code for payment."
    show tsm nhuh
    TSM "“H-hey, I thought we were splitting the bill?“"
    MC "“You can worry about that at home, we can calculate it later.“"
    show tsm nuhsure
    C "“Here’s the code.“"
    MC "“Okay wait a sec.“"
    MC "“And done!“"
    C "“Thank you for your patronage.“"
    C "“You two make a lovely couple by the way! Is this perhaps your first week of moving together?“"
    show tsm nbsurprised
    TSM "(!!!)"
    show tsm nsurprised
    "Rudy turns to look at me, completely frozen. The words completely stuck in his mouth, something in his eyes tells me that he wants me to say something for him."
    menu:
        "We do, don’t we, {i}darling{/i}?":
                show tsm nsdquestioning
                TSM "“[MC]...“"
                show tsm npout
                "He tugs at my sleeve, silently begging to get us as far as possible from the store."
                MC "“Anything wrong?“"
                show tsm npout
                "He tugs even harder."
                MC "“Sorry, he’s shy. We’ll be off now, thanks!“"
                show tsm nuhsure
                TSM "{size=+10}“Why didn’t you correct her?“{/size}"
                MC "“Oh? That’s not what you wanted me to say?“"
                show tsm nbangy
                TSM "“No!“"
                show tsm npout
                MC "“Then you correct her then.“"
                show tsm nsdbangy
                TSM "“I-I...Ugh shit...“"
        "Oh, we’re not married.":
                C "“I’m so sorry!“"
                MC "“It’s okay, thanks anyway.“"
    
    scene roadn with fade
    show tsm nsdbangy
    TSM "“I don’t think I'll ever be able to step foot in that store ever again.“"
    MC "“Oh come on, it’s not that bad.“"
    MC "“Besides, it’s just one employee out of dozens. You might not even see her again.“"
    show tsm nsmirk
    TSM "“Whatever. Let’s go back, I'll make us something.“"
    MC "“Ooh, can’t wait!“"
    
    scene inside with fade
    MC "(I’m getting really hungry.)"
    "Rudy’s in the kitchen preparing our food while I'm setting up the dinner table."
    "Well...table, I don’t actually have one so we’re using the small stools and cardboard boxes instead."
    "We could eat at my desk but we’d have to clear out all the papers and stuff first."
    MC "(Maybe I should just buy us a picnic blanket and we’ll eat on the floor.)"
    "I already prepared a glass of water for both of us. Earlier, I asked him which glass he wanted to use and by now he has staked his claim on this glass that I bought as a souvenir from a tourist location."
    show tsm mnormal
    TSM "“Here’s dinner.“"
    show tsm msilent
    "As he enters the room with food in his hands, my mouth starts to water in anticipation as the smell wafts around the room."
    MC "(What did I do in my past life to deserve this?)"
    MC "(Warm food and a cute boy in a maid outfit, what else can a [player_ds] want?)"
    show tsm munsure
    TSM "“What’s with that look on your face?“"
    show tsm msilent
    MC "“What?“"
    show tsm mnormal
    TSM "“You’ve been staring.“"
    "If you’re hungry just eat, the food is right there. Unless you have something to complain about?"
    menu: 
        "Not at all, dinner looks great.":
                show tsm m
                TSM "“Good. Eat up then.“"
                MC "“Will do, Chef!“"
                show tsm m
                "Upon hearing my enthusiastic exclamation, he lets out a small chuckle."
                TSM "“Stop that, stupid.“"
                MC "“Yes, Chef.“"
        "Is the cute chef part of the meal as well?":
                show tsm mbsurprised
                TSM "(!)"
                show tsm mbangy
                TSM "“Shut up and eat already!“"
                MC "“Eat what? The chef or the food?"
                show tsm mdeflecting
                TSM "“THE FOOD!“"
                show tsm mangy
                TSM "“Urgh, I can't believe you...“"
                show tsm mbpout
                MC "“Sorry, I’ll stop. The food looks and smells great by the way.“"
                MC "“Thanks for the meal.“"
                MC "(I keep forgetting that I should tone the teasing down, wouldn’t wanna piss him off before we’re even a week through the deal.)"

    show tsm msilent
    TSM "..."
    MC "(I feel kinda awkward if we’re just eating in total silence, maybe I can strike up a conversation?)"
    MC "“So... how was your day?“"
    MC "(Yea, that’s a {i}great{/i} way to start, [MC])"
    show tsm mnormal
    TSM "“‘s fine.“"
    TSM "“You?“"
    show tsm msilent
    MC "“Better than a few days ago that’s for sure.“"
    show tsm mnormal
    TSM "“Oh, good.“"
    show tsm msilent
    TSM "(...)"
    MC "(What else?)"
    MC "“It’s been a while since we’ve eaten together.“"
    show tsm munsure
    TSM "“It has?“"
    show tsm msilent
    MC "“The last time we ate together was when we first entered college, and now we’re almost on our third semester.“"
    show tsm mnormal
    TSM "“Right, it was when we were searching for clubs together.“"
    TSM "“I was gonna go alone but then you asked me to go with you out of nowhere.“"
    MC "“Yup, I’m glad I asked! Going alone would’ve been pretty lonely besides, that’s the first time I ever saw your homemade lunches.“"
    MC "“We sat down on the side of the field under the tree.“"
    show tsm mhappy
    TSM "“I can’t believe you asked me which stall sold the meal. As if it wasn’t obviously my own lunch box.“"
    show tsm msilent
    MC "“Can’t help it, it smelled good and I wanted a bite!“"
    MC "“I wasn’t about to ask for a bite from a guy I wasn’t too close with.“"
    show tsm msmirk
    TSM "“And where did all that hesitation go, huh?“"
    TSM "“You went from not daring to ask for a bite, to asking me to cook for you everyday.“"
    show tsm msilent
    MC "“Hey, you agreed.“"
    MC "“I think this is one of the smartest things I've done in your life.“"
    show tsm msmirk
    TSM "“You must’ve done a lot of stupid things then.“"
    MC "“Hey, watch it.“"
    show tsm mhappy
    TSM "“C’mon, you gotta be pretty stupid to have {i}this{/i} as one of the smartest things you’ve ever done.“"
    MC "“Really? You’ve seen me do other less stupid things. It's not like you've never done aything stupid before.“"
    show tsm mpout
    MC "“Who was it that forgot their hat and sunscreen when we went club hunting?“"
    TSM "“grr...“"
    MC "“Who got us lost during orientation?“"
    show tsm mnormal
    TSM "“Whatever, we made it there on time. I’m glad you brought that umbrella with you, it would’ve been super hot otherwise.“"
    show tsm msilent
    MC "“It really blocked the sun didn’t it?“"
    show tsm msure
    TSM "“Well, I guess that’s one of your good traits...“"
    MC "“Oh?“"
    show tsm mhappy
    TSM "“I don’t see you often, but whenever I do, you’re.. oddly well prepared.“"
    show tsm msilent
    MC "“It’s just an umbrella.“"
    show tsm munsure
    TSM "“You have stomach medicine on the ready in your bag, and you don’t even need it.“"
    show tsm msilent
    MC "“Well, they made us buy it, I might as well bring it in case.“"
    MC "“Since I don't need it, I might as well give it to people who do, like you.“"
    show tsm msure
    TSM "“Y-yea. Uh, thanks for that. I wouldn’t’ve survived the opening ceremonies otherwise.“"
    show tsm msilent
    MC "“Don’t mention it.“"
    MC "“‘Sides I think we’ve grown a bit closer since that time, no?“"
    show tsm munsure
    TSM "“I could’ve sworn you wanted to join 2 clubs, did you ever fall through with that plan?“"
    show tsm msilent
    MC "“Nah, I totally forgot to go back and sign up.“"
    MC "“I’m kinda glad that happened though, I don’t think I'd ever get any sleep if I was any busier.“"
    MC "“I’m happy with my current choice though.“"
    MC "“If I remember, you chose badminton?“"
    show tsm mhappy
    TSM "“Yea, I’ve been doing it since I was a kid.“"
    TSM "“Might as well keep going.“"
    show tsm msilent
    MC "“I still can’t believe we don’t have a book club of all things.“"
    show tsm msmirk
    TSM "“Same here, I feel like that should’ve been a basic pick.“"
    TSM "“We have a club for diving and we don’t even live near the ocean.“"
    show tsm msilent
    MC "“You think they travel for hours just to do their club activities?“"
    show tsm mhappy
    TSM "“Nah, I bet they just practice at the pool unless some special event happens.“"
    show tsm msilent
    MC "“Maybe?“"
    MC "“Man, getting to talk to you again is pretty fun. We barely walk to campus together anYMore, so this has been kinda nice.“"
    show tsm mnormal
    TSM "“You just walk alone then?“"
    show tsm msilent
    MC "“I did, but as time went on I found that my schedule matches with another friend. And I usually walk with him, if I do see him.“"
    MC "“Which is surprisingly pretty often.“"
    show tsm mnormal
    TSM "“Guessin’ he’s in the same major?“"
    show tsm msilent
    MC "“No actually, which makes the fact that our schedules line up even more surprising.“"
    MC "“I swear he’s psychic or some shit.“"
    show tsm msdnormal
    TSM "{size=-10} “Lucky bastard...“{/size}"
    MC "“Sorry what? Couldn’t hear you.“"
    show tsm mbangy
    TSM "“Nothin’! You done eating?“"
    show tsm mpout
    MC "“Yea, I am.“"
    show tsm mnormal
    TSM "“Here, let me do the dishes.“"
    show tsm msilent
    MC "“Nah, I’ll handle it.“"
    MC "“I can’t let you do {i}all{/i} the work. I’m sure I can handle the dishes.“"
    show tsm munsure
    TSM "“Are you sure?“"
    show tsm msilent
    MC "“Yep. Relax for a bit, why don’t cha?“"
    show tsm msure
    TSM "“Oh... alright then. Thanks.“"
    show tsm msilent
    MC "“No problem.“"
    MC "(Huzzah, one successful dinner without teasing him {i}too{/i} much.)"
    MC "(Whether or not I can do this again tomorrow is up for debate.)"
    
    scene inside with fade
    MC "“I’m back.“"
    show tsm snormal
    TSM "“Hey, do you mind if I use your desk? I’m planning on studying tonight.“"
    show tsm ssilent
    MC "“Go ahead, I finished my work yesterday.“"
    MC "“I think I'll go to bed early today.“"
    show tsm shappy
    TSM "“Good, you should have some sleep.“"
    show tsm suhsure
    TSM "“I’m guessing you slept pretty late yesterday?“"
    MC "“Yea.“"
    MC "(And the day before that, and the day before that too...)"
    show tsm snormal
    TSM "“G’night then. You wanna turn the lights off?“"
    show tsm ssilent
    MC "“Nah, it’s cool. I have this sleeping mask to block the lights out.“"
    MC "“Besides, you need it don’t you? After all, ‘Working with the lights off hurts your eyes’.“"
    show tsm ssmirk
    TSM "“Is that supposed to be an impression of me?“"
    show tsm ssilent
    MC "“What? That’s what you said yesterday.“"
    MC "“So don’t worry about me, I'm sure you need to study.“"
    show tsm shappy
    TSM "“Well...thanks then. I’ll be quiet.“"
    show tsm ssilent
    MC "“Goodnight, Rudy.“"
    show tsm shappy
    TSM "“Yea, g’night.“"
    hide tsm
    scene black with fade
    jump week_tsm
    
label day2_ym:
    #YM Maid day 2"
    scene black with fade
    YM "“[MC]? Are you awake?“"
    YM "“I guess not.“"
    YM "“Hehe, you look so cute like this. I can stare at you for hours...“"
    YM "“Wait, I have to wake [player_object] up!“"
    YM "“[MC], wakey wakey!“"
    YM "(...)"
    YM "“Please? [MC]? Wake up.“"
    YM "“Well, here goes nothing.“"
    YM "{size=+5}“BOO!“{/size}"
    scene inside with vpunch
    MC "(!!!)"
    MC "“WHAT HAPPENED? Is there a fire?? You okay??“"
    show ym nrhappy
    YM "“Silly [MC], everything is fine!“"
    YM "“I just wanted to wake you up, look I made breakfast!“"
    show ym nsmile
    "As he points at the table I see the aforementioned breakfast. It was a slice of bread covered with a chocolate spread and a messy smiley face drawn with condensed milk."
    menu:
        "Aww, it has a smiley face!":
                show ym napologetic
                YM "“Do you like it...?“"
                show ym nsmile
                MC "“Of course I do! Thanks for breakfast.“"
                MC "“Where’s your slice?“"
                show ym nhappy
                YM "“Unfortunately, I already ate it earlier. I have class in a bit so I have to leave early.“"
                show ym nsmile
                MC "“Okayy, see you later.“"
                show ym nhappy
                YM "“Byee, [MC]!“"
        "(Unfortunately, that’s not my thing)":
                $ YM_dp +=1
                "(I’d feel bad if I said that though since he’s beaming with joy.)"
                MC "“Well, thanks?“"
                show ym nsilent
                "I tried giving him the most convincing smile I could muster, if he noticed my insincerity, he didn’t voice them."
                show ym napologetic
                YM "“Well, I'll be leaving early since I have class. See you later?“"
                show ym nsmile
                MC "“See ya’.“"
                MC "(Well, I guess having breakfast never hurts.)"
    
    scene campus1d with fade
    MC "(I feel like I haven’t felt this good in the morning for a while.)"
    MC "(Still, he goes way above what I expected him to do. I like having him do stuff for me and all, but I kinda feel bad.)"
    "(He even went as far as to wearing that maid outfit.)"
    menu:
        "(Personally, I love it! He’s so cute!!)":
                MC "(I don’t know what he was thinking when he bought it but I like it!)"
        "(I think he’s going way too far.)":
                MC "(I’m grateful that he’s doing housework but this seems too far, like it’s the plot of a self-indulgent piece of media.)"
    
    "In the distance I slowly start to see Nix’s silhouette appear, strolling casually with a few people I recognize as his friends."
    "Based on the pins they have on their bag, I’ve always assumed they’re from the same major."
    "Sometimes I wonder why I didn't meet Nix sooner. If we went to the same highschool surely I must've encountered him at some point."
    "Seeing that he’s quite the social butterfly, I find it weird that neither me nor any of my friends seem to recall ever meeting someone like him."
    MC "(Unless...he’s been lying?)"
    MC "(No way, he knows all the teachers I know and every story he tells about our school events seem to line up with my memories.)"
    MC "(I don’t think you can make up stories about extremely specific school events like that.)"
    MC "(Oh shit, did he catch me staring? I guess getting stared at from a distance isn’t a nice feeling.)"
    "He waves his entire arm at me and almost beckons me to come over."
    menu: 
        "Go talk to him":
                MC "(Nothing to be ashamed of, he usually approaches whether I’m staring or not.)"
                MC "“Hey man, what’s up?v"
                MC "“Breakfast was good by the way.“"
                show ym nrhappy
                show cs normal at left
                show qs normal at right
                YM "“Aww thanks, [MC]! I’m glad you like it.“"
                show ym nsmile
                MC "“Sorry for staring, I just wanted to say hi. You can go back to your friends now.“"
                show ym nrhappy
                YM "“No way! We should walk together, our buildings are in the same direction anyway.“"
                show ym napologetic
                YM "“You guys don’t mind do you?“"
                show ym nsmile
                CS "“It’s cool man.“"
                QS "..."
                "The other friend doesn’t say a word instead,  he gives a thumbs up in approval."
                show ym nhappy
                YM "“See? They’re okay with it.“"
                show ym nsmile
                MC "“Alright then, thanks for letting me join.“"
                CS "“Soo, what’s with the whole breakfast thing? You guys ate together or somethin'?“"
                MC "“Nah, but he did make me breakfast.“"
                show ym nrhappy
                YM "“I’ll do it again tomorrow!“"
                show ym nsmile
                CS "“Oh, you two live together now?“"
                QS "“That’s news to us.“"
                MC "“Yea, he asked to move with me ever since his place caught on fire.“"
                QS "“What?“"
                CS "“That was {i}your{/i} place?“"
                QS "“You never told us that.“"
                CS "“Good thing your [player_pronoun] agreed to let you stay."
                MC "(Wha-? [player_pronoun]?)"
                show ym nrhappy
                YM "“I know! I’m glad I have [MC] in my life.“"
                show ym nsmile
                MC "(He’s not denying it. Guess I’ll play along?)"
                MC "“Anything for you {I}love{/I}.“"
                show ym nsqueal
                "He freezes in his steps and gives out a strangled squeal, seemingly caught off guard by the sudden romantic pet name."
                show ym nrhappy
                YM "“You called me ‘love’!!“"
                show ym nsqueal
                MC "“Yea?“"
                MC "(Should I not have?)"
                show ym nrhappy
                YM "“I love you, I love you, I love you!!!“"
                "He gives me a tight hug "
                show ym nsmile
                QM "“Gross.“"
                CM "“Keep this up and we’re leaving you two behind.“"
                QM "“No. We’re leaving now.“"
                show qs at offscreenright with easeout
                "With that, the quiet one sprints ahead leaving the rest of us behind."
                hide qs
                CM "“Well, I'm not gonna be a third wheel so...“"
                CM "“Byee!“"
                show cs at offscreenright with easeout
                "After a short wave, he soon follows and sprints in the direction of his next class."
                hide cs
                show ym nrhappy
                YM "“I guess it’s just the two of us now, [MC].“"
                show ym nsmile
                MC "“Why didn’t you correct them?“"
                show ym nworry
                YM "“Are you mad at me for that?“"
                show ym nsilent
                MC "“No, just curious.“"
                show ym nhappy
                YM "“Well, it’ll make explaining why we live together easier!“"
                show ym napologetic
                YM "“Are you okay with that?v"
                MC "“Well...“"
                MC "(I’d be lying if I said it didn’t give my heart a little flutter, he’s cute after all)"
                show ym nhappy
                MC "“I guess I’m okay with it.“"
                show ym nrhappy
                "He beams with joy at my words and we slip into a comfortable silence for the rest of our walk."
        "Run and pretend I never saw him":
                $ YM_dp +=1
                MC "(NOPE. I definitely made him uncomfortable with all the staring.)"
                MC "(We’ve been spending so much time together, I should probably let him have some time with his other friends.)"
                MC "(Time to head straight to class!!!!)"
                MC "“I quickly sprint to the side, taking another path than my usual to my building.“"
                scene campusd with vpunch
                MC "(Hopefully that wasn’t {I}too{/I} awkward.)"
                MC "(Hopefully he didn’t run after me!)"
                show tsm ndeflecting
                TSM "!!!"
                show tsm nuhsure
                TSM "“The hell? [MC]?“"
                MC "“Oh, hi! Sorry for running into you!“"
                show tsm nnormal
                TSM "“s’okay, you should hurry before you’re late.“"
                TSM "“You seem like you’re in a rush.“"
                show tsm nsilent
                MC "“Thanks!! Bye!!“"
                show tsm nnormal
                TSM "“Yea.“"
                hide tsm
                "And with that, I continue running to class."
    
    scene class with fade
    MC "(WOO!! Class is OVER!)"
    MC "(And since I finished most of my assignments yesterday, i’m practically free tonight.)"
    MC "(Maybe I can even clean up tonight, lessen whatever burden Nix decided to tackle while he moved into my place.)"
    F "“You seem to be doing better.“"
    MC "“Yea, I finished my assignments.“"
    F "“Good for you. I still have to hurry back and finish mine.“"
    MC "“Good luck!“"
    F "“Thanks. See you tomorrow!“"
    MC "“Byee!“"
    play sound "audio/notifhp.mp3"
    MC "(Is it Nix?)"
    show phone ym
    MC "(Yep, it is.)"
    MC "“Hey, what’s up!“"
    YM "“Hi! I’m planning on stopping by the grocery store so I can cook for us tonight, can you please come with me?“"
    YM "“You can tell me what you like and what you don’t so I know what to make.“"
    MC "“You’re cooking dinner too?“"
    YM "“Yep! I wanna treat you as well as possible while I'm living with you.“"
    MC "“Are you sure?“"
    YM "“Absolutely! In fact, I'm actually outside your class!“"
    hide phone
    show ym n
    "I peek at the door and find Nix, eagerly waving at me through the door as if he’s been waiting for me this whole time."
    MC "“Damn, I guess we’ll have to go grocery shopping huh?“"
    show ym nhappy
    YM "“Yep! You can’t run away, [MC].“"
    show ym nsmile
    MC "“Alright, let’s go.“"
    
    scene supermarket with fade
    show ym nhappy
    YM "“Here we are! Is there anything you want?“"
    show ym nsmile
    MC "“What can you cook?“"
    show ym nrhappy
    YM "“Anything for you!“"
    show ym nsmile
    MC "“{i}Anything{/i}?“"
    show ym nhappy
    YM "“Anything.“"
    show ym nsmile
    MC "“Uhh, cool, let’s go with something easy then.“"
    "How about..."
    menu:
        "Pasta":
                show ym nhappy
                YM "“Sure! They have some over there.“"
        "Soup":
                show ym nhappy
                YM "“Nice! Something to really warm us up tonight.“"
        "Fried rice":
                show ym nrhappy
                YM  "“Oooh! I love fried rice!“"
                show ym nsmile
                MC "“I know, you tend to order it when we eat at the cafeteria.“"
                show ym nrhappy
                YM "“Awww, you remember what I likee!!“"
                MC "“Let’s continue shopping, shall we?“"

    show ym nsmile:
                   parallel:
                           ease .5 zoom 1.5
                   parallel:
                           yalign 0.0
                           linear 0.0 yalign 0.0 xalign 0.5
    "We head over to grab the ingredients for the dish, carefully comparing prices between brands. Neither of us are particularly well practiced in getting the best deals possible, but with our 2 brain cells combined, we managed to make one competent human being!"
    "Once we’ve grabbed everything we need, we head on over to the cashier and they start scanning our items."
    C "“So that’ll be this much. How would you like to pay?“"
    show ym napologetic
    YM "“[MC], I’ll pay okay?“"
    MC "“No, QR code please.“"
    show ym nquestioning
    "Knowing full well that Nix would never let me pay him back, I quickly grab my phone to scan the payment qr code."
    "Whenever I buy food on campus, Nix would pay for it without ever letting me pay him back."
    "One time, I ended up sneaking the money in an envelope into his bag out of desperation only to find it back in mine the next day." 
    MC "(He’s sneaky, I’ll give him that.)"
    show ym nworry
    YM "“But-“"
    show ym nsqueal
    "I shove my free hand to cover his mouth so he can’t protest any further. He immediately shuts up, staring at me wide-eyed."
    MC "“No, we need to split it.“"
    show ym nrhappy
    "He does a quick nod and I can feel his lips forming into a smile under my hands.“"
    "Soon after it scans, I show the cashier the proof of my successful payment.“"
    C "“Thank you! Have a nice day!“"
    MC "“There! I finally got to pay for something!“"
    show ym nhappy
    YM "“I guess I can let it slide this time. After all, I'll be paying you back {I}all{/I} month.“"
    show ym nsmile
    MC "“Shall we go back so you can start repaying me then?“"
    show ym nhappy
    YM "“Sure!“"
    
    scene inside with fade
    MC "(I feel a little bad that Nix is doing all this while i’m just setting the table, but he did insist.)"
    MC "(Well..’table’, we’re eating on the floor with buckets and boxes as tables. By this point I should just buy a picnic blanket or something.)"
    MC "(I would set a candle or something to make it look nicer but I'd rather not start another fire. So I settled for a paper flower that I made five minutes ago, hopefully he doesn’t mind?)"
    MC "(As soon as we got back, he changed into that maid outfit and started cooking.)"
    MC "(I would protest but I’d be lying if I said I wasn’t happy with a cute boy in a maid outfit.)"
    show ym mhappy
    YM "“[MC]! I’m done cooking!“"
    "Instantly, the smell of food wafts through the air, making the growls of my stomach grow louder as my mouth begins to water."
    MC "“Damn, I guess you can cook. It smells great!“"
    show ym mrhappy
    YM "“Thanks! I tried!“"
    YM "“Ooh! Did you make the flower?“"
    show ym msmile
    MC "“Yea, I figured I’d add something to make it look nice.“"
    show ym mhappy
    YM "“Awww, thanks, [MC].“"
    show ym mapologetic:
                   parallel:
                           ease .5 zoom 1.5
                   parallel:
                           yalign 0.0
                           linear 0.0 yalign 0.0 xalign 0.5
    "With a smile he serves me my food, looking at me with a hopeful gaze."
    MC "(I guess he’s waiting for my seal of approval?)"
    show ym mgrin
    "I take a quick bite and a smile soon blooms on my face. Seeing my reaction, Nix grins happily."
    show ym mhappy
    YM "“I’m glad you like it!“"
    MC "“Itsshogood.“"
    show ym mrhappy
    YM "“Hehe, thanks!“"
    MC "“You should eat it too, enjoy your hard work and all.“"
    show ym mhappy
    YM "“I already am enjoying my hard work but alright.“"
    show ym mcontent
    YM "“Hmm, it is good.“"
    MC "“Thanks for cooking, you really don’t have to do it.“"
    show ym mquestioning
    YM "“Why would I not? We’re friends, yea?“"
    show ym msmile
    MC "“Hmm.“"
    menu:
        "(I guess we are)":
                MC "(By some definition of the word.)"
        "(I’d like us to be something more)":
                MC "(Not that I’ll tell him that right now.)"
    
    MC "“Y’know, we eat together a lot but eating on the floor like this sure is a new feeling.“"
    show ym mhappy
    YM "“It’s kinda fun, thanks for setting up the table, [MC].“"
    MC "“Should I buy us a picnic blanket? That’ll make it more exciting.“"
    show ym mrhappy
    YM "“Ooh! That sounds great!“"
    show ym mapologetic
    YM "“You’re always fun to talk to, [MC].“"
    MC "“And you have always been too nice to me.“"
    MC "“Seriously, how did we not meet in highschool? I kinda wish we did.“"
    show ym msdworry
    YM "“I think it’s for the best that we met in college, highschool me was kinda...“"
    MC "“Oh, yea now that I think about it, I was also kinda mean in highschool.“"
    show ym mwhine:
                   parallel:
                           ease .5 zoom 1.7
                   parallel:
                           yalign 0.0
                           linear 0.0 yalign 0.0 xalign 0.5
    YM "“NO YOU WEREN'T!“"
    show ym mworry
    YM "“Oh-uh, sorry for raising my voice.“"
    show ym mapologetic:
                   parallel:
                           ease .5 zoom 1.5
                   parallel:
                           yalign 0.0
                           linear 0.0 yalign 0.0 xalign 0.5
    YM "“You weren’t mean at all! In fact, you helped me out when I was in trouble back then, even when I was a complete stranger...“"
    show ym msmile
    MC "“Sure you have the right person? Pretty sure I was kinda competitive at the time.“"
    show ym mhappy
    YM "“You didn’t know highschool me, but I knew highschool you. And you were definitely the nicest person I’ve met there.“"
    MC "“Stop lyin’ bro.“"
    show ym mhuffy
    YM "“I’m not lying! I heard about how you would help your classmates if they asked, you taught them math, helped refine their grammar for those presentations done in foreign languages.“"
    YM "“You gave them your notes and helped review for tests even when you didn't need to.“"
    show ym mhuffy
    MC "“And how do you know this?“"
    YM "“I know for a fact we weren’t in the same class.“"
    show ym mnormal
    YM "“No, but I had friends who were.“"
    show ym msdworry
    YM "“I was kinda jealous of them but highschool me was so… so.. Ugh I don’t even wanna say it.“"
    MC "“It’s okay, we all have cringe pasts (like me). And for some of us, we have cringe presents (also like me).“"
    show ym msmile
    MC "“Either way, we all have room to grow and embrace the embarrassing parts..or something like that.“"
    MC "“I’m not great at this kinda thing.“"
    show ym mcontent
    YM "“N-no that made a lot of sense actually.“"
    show ym mrhappy
    YM "“Gosh, you just made yourself look even more amazing to me.“"
    show ym msmile
    MC "“Nah, if you knew what I was like in middle school I'm sure your perception of me would drop.“"
    show ym mproud
    YM "“That doesn’t change who you are now!“"
    show ym mcontent
    YM "“And I like you for you.“"
    MC "“Aww, that’s oddly sweet.“"
    show ym msmile
    MC "“Seriously, by the way you act now, I'm really sure you weren’t that bad in highschool.“"
    MC "“Hey, we could’ve been slightly shitty people together?“"
    MC "“I was a little mean (even if you didn’t think so) and you were..whatever it is you were.“"
    show ym mrhappy
    YM "“Hehe, you always seem to make it better, [MC].“"
    MC "“Are you done with your food?“"
    show ym mhappy
    YM "“Oh yea.“"
    MC "“I’m washing the plates!“"
    show ym mhuffy
    YM "“Wait [MC]!“"
    MC "“Nope! NO objections! A cute maid cooked me dinner and now it’s time to return the favor.“"
    show ym mapologetic
    YM "“Oh, [MC]...“"
    
    scene inside with fade
    MC "“I’m back!“"
    show ym sapologetic
    YM "“Heyy, I’m about to study, is it okay if I borrow your desk? I can move if you’re working on something again.“"
    show ym ssmile
    MC "“Nah, it’s cool. I’m about to sleep early tonight.“"
    show ym srhappy
    YM "“Good night, [MC]!“"
    show ym squestioning
    YM "“Actually...can I ask for a reward if I study hard tonight?“"
    MC "“What is it?“"
    show ym shappy
    YM "“Can I cuddle up to you?“"
    menu:
        "Go ahead! I hope you don’t mind if I hug back":
                show ym srhappy
                YM "“Sweet! I’ll be sure to work hard!“"
        "Sorry no, stay in your own place.":
                $ YM_dp +=1
                show ym ssorry
                YM "“Oh, okay then.“"
    
    MC "“Anyway, g’night Nix. Turn off the light when you're done, kay?“"
    show ym shappy
    YM "“Okayy.“"
    scene black with fade
    
    if YM_dp >= 6:
        YM "“Hngh...[MC]...what did I do wrong...?“"
        YM "“Why...just w-why won’t you love me...?“"
        YM "“You even ran away from me this afternoon..Did I...do something?“"
        YM "“I was hoping dinner would win you over but you still wouldn’t even {i}touch{/i} me...“"
        YM "“W-where did I go wrong? I changed so much for you...!“"
        YM "“I’m {b}different{/b}  from back then, I changed so much just for you alone.“"
        YM "“You’re the only reason I’m even at this place...“"
        YM "“You have to love me, you just have to...“"
        YM "“{b}I won’t let you go no matter what.{/b}“"
        jump week_ym
    
    else:
        jump week_ym
    
label week_tsm:
    #TSM Maid Week Later"
    scene insidepd with fade
    MC "(I have miraculously survived a whole week while living with Rudy.)"
    MC "(Or maybe saying {i}he{/i} survived would’ve been more fitting?)"
    MC "(After all, I’m the one getting all the benefits from this cohabitation.)"
    MC "(True to his word, he’s been regularly cleaning the place and cooking meals for us. It’s really thanks to him that I have more time to finish my current never ending wave of assignments.)"
    MC "(In anycase, I managed to tone down whatever flirty comments came to my mind in an attempt to maintain peace and friendship.)"
    MC "(Since today marks the seventh day of him surviving in my place, I've decided to be extra nice and buy us dessert to celebrate.)"
    MC "(Or maybe as an apology for making him wear a maid outfit.)"
    MC "(I’ve been sneakily asking him about the type of desserts that he likes and I think I found something within a reasonable budget that matched.)"
    MC "(Our nearby supermarket sells silky pudding and I’m planning on surprising him with it.)"
    show tsm nnormal
    TSM "“I’m gonna head out.“"
    show tsm nsilent
    MC "“Okayy.“"
    show tsm nuhsure
    TSM "“You want anything specific for dinner? I’m gonna go shopping for groceries later.“"
    show tsm nnormal
    TSM "“I think I know what you like by now so you don’t need to tag along if you’re busy.“"
    MC "“I’ll take anything you cook, I trust you.“"
    MC "“By the way, are you just telling me not to go with you so that the cashier won’t mistake us for a couple again?“"
    show tsm nsdbangy
    TSM "“No...“"
    menu:
        "If you say so.":
                show tsm nbangy
                TSM "“Hey-! It’s not like that!“"
        "In that case, I’ll go with you!":
                show tsm nbdeflecting
                TSM "“NO DON’T!“"
                show tsm nnormal
                TSM "“I mean. Uh. You’re busy, yea? Don’t bother.“"
    
    MC "“Whatever you say, {i}darling{/i}.“"
    show tsm npout
    TSM "“Hrmph...“"
    show tsm nsdnormal
    TSM "“You’re cruel and unusual, y’know that?“"
    MC "“Gee, I have no clue what you’re talking about.“"
    show tsm nnormal
    TSM "“By the way,  I'm going to a different grocery store so no one will recognize me.“"
    show tsm nsilent
    MC "“Damn, isn’t that one even further?“"
    show tsm nuhsure
    TSM "“So?“"
    show tsm nsilent
    MC "“Any clue what time you’ll be back?“"
    MC "(I kinda need an estimate so I can keep the pudding a surprise.)"
    show tsm nhuh
    TSM "“W-why d’ya wanna know?“"
    MC "(Here we go [MC], do NOT respond with ‘Cause i’ll miss you’, I promised not to tease him too much)"
    MC "“Just wanted to make sure I’m not already asleep by the time.“"
    show tsm nnormal
    TSM "“No way, I’ll be back before 6:30.“"
    show tsm nsmirk
    TSM "“I can’t have you falling asleep before even having dinner.“"
    show tsm nsilent
    MC "“Good to know.“"
    MC "(Alright, my classes end at 5. If I hurry I should be able to make it in time.)"
    show tsm nuhsure
    TSM "“Anything else? I’m about to leave.“"
    show tsm nsilent
    MC "“Nope! You can go now.“"
    show tsm nhappy
    TSM "“See ya’“"
    MC "“See you later too!“"
    
    scene campusd with fade
    MC "(What flavor should I get him later?)"
    MC "(He likes chocolate, maybe I should stick with that? Or maybe he’d want something else for a change...?)"
    MC "(No, he doesn’t like fruity flavors in pudding so maybe not...)"
    MC "(Vanilla perhaps? If they have any.)"
    YM "{size=-5}“[MC]!“{/size}"
    MC "(What if they don’t?)"
    YM "{size=-7} “Hey, [MC]?“{/size}"
    MC "(I guess I’ll stick to chocolate...)"
    YM "“[MC]!“"
    scene campusd with vpunch
    show ym nworry
    MC "“Nix? Sorry I wasn't paying attention to my surroundings.“"
    MC "“What’s up?“"
    show ym nhappy
    YM "“I saw you in the distance and figured I'd say hi. Wanna walk together?“"
    show ym nnsmile
    MC "“Same as always huh?“"
    show ym rhappy
    YM "“Yep!“"
    show ym nsmile
    MC "“Let’s go then.“"

    scene campusd with fade
    show ym napologetic:
                   parallel:
                           ease .5 zoom 1.75
                   parallel:
                           yalign 0.0
                           linear 0.0 yalign 0.0 xalign 0.5
    YM "“So, how are you doing? You seem happier recently. Anything good happened?“"
    show ym nsmile
    MC "(Yea, I have someone to help out with housework now. Not that I can tell him that.)"
    MC "“I’ve been keeping up with my assignments better that’s all.“"
    show ym nhappy
    YM "“If you’re ever stressed out, I’m here for you.“"
    YM "“I can make you lunch and stuff.“"
    MC "(Oops, I can’t tell him I got Rudy for that.)"
    MC "(Even if I wanted to tell him, I’m a hundred percent sure that Rudy would hate it if anyone knew we were living together.)"
    MC "“You don’t need to do that, I’m surviving just fine.“"
    show ym nnormal
    YM "“But really, I want to.“"
    MC "“And again, since when do you cook?“"
    show ym nhappy
    YM "“I can start whenever you want me to.“"
    MC "“Yea, No. I’m fine without it dude.“"
    show ym nhappy at right:
                   parallel:
                           ease .5 zoom 1.75
                   parallel:
                           yalign 0.0
                           linear 0.0 yalign 0.0 xalign 0.5
    show tsm nsilent at left
    
    "As Nix tries to convince me to let him cook for me, I see a familiar view in the distance."
    "It’s Rudy (or at least I assume it is), staring awkwardly at my direction. I’m guessing that he’s feeling anxious about waving at me when I’m with a friend."
    show ym nmad
    "I decided to wave at him as both a ‘hi!’ and ‘see you later!’"
    show tsm nhuh
    "I wish I could say that he reciprocated but instead he stood there in shock and ran away without acknowledging it at all."
    hide tsm
    show ym ngrin at center:
                   parallel:
                           ease .5 zoom 1.75
                   parallel:
                           yalign 0.0
                           linear 0.0 yalign 0.0 xalign 0.5
    MC "(Ouch, I guess waving at him was the wrong call.)"
    MC "(Or even worse, maybe that wasn’t Rudy and I just waved at a complete stranger.)"
    show ym nquestioning
    YM "“Who was that, [MC]? You were waving your hands.“"
    show ym nsilent
    MC "“I thought I saw someone I knew but I guess I had the wrong person?“"
    show ym nhappy
    YM "{size=-10}“good.“{/size}"
    show ym nsmile
    MC "“What was that?“"
    show ym nrhappy
    YM "“Nothing! That probably wasn’t anyone important then. Let’s head to class, shall we?“"
    MC "“Okay?“"
    
    scene class with fade
    MC "(Class is over, it’s go time!)"
    "I check my phone for time and see that it’s currently five past five."
    MC "(No time to dawdle, I gotta hurry before Rudy gets back.)"
    
    scene supermarket with fade
    MC "(Alright! Where’s the pudding section?)"
    MC "(Pretty sure it’s over there...somewhere?)"
   
    MC "(Aha! There it is.)"
    MC "(I got the chocolate pudding!)"
    MC "“I hold the cups high above my head as if I was a knight celebrating over a triumphant duel before suddenly remembering that I was in the middle of the grocery store.“"
    MC "(Oops, let’s just go pay)"
    C "“Oh! You’re the one from last week!“"
    MC "“Oh, hi?“"
    MC "(That’s the cashier from last week, I guess Rudy made the right choice since she still remembers me)"
    C "“I see you’re shopping alone this time. Are things well with your...husband?...err boyfriend?“"
    MC "(Oh, she’s still mistaking us for a couple.)"
    MC "“Uhh, things are fine. I bought these for him.“"
    C "“How sweet! How would you like to pay?“"
    MC "“QR code please.“"
    C "“Alright, give me a sec.“"
    C "“Here.“"
    MC "“Done!“"
    C "“Thankyou for your purchase!“"
    MC "“Sure!“"
    "Once outside, I check my phone once again to make sure I’m still on time."
    MC "(20 minutes left till 6, let’s go!)"
    
    scene inside with fade
    play sound "audio/doorop.mp3"
    MC "(Is he back yet?)"
    "I unlock the doors to my place and peek inside, since the lights are off I can only assume Rudy isn’t here yet."
    MC "(Good, now I just gotta hide these in the fridge and wait for him to get back.)"
    MC "(Then I’ll start working on my assignments while I wait for him.)"
    
    scene cg1 with fade
    MC "(Alright, I think I’ll work on my homework while he isn't back. He might wanna use it to study later.)"
    play sound "audio/typing.mp3"
    #pause 1s
    scene cg1 with fade
    play sound "audio/typing.mp3"
    "..."
    play sound "audio/knock.mp3"
    GTWU "{size=-10}“[MC], I’m back.“{/size}"
    MC "(Damn, how do I do this part?)"
    play sound "audio/knock.mp3"
    TSM "“[MC]?“"
    MC "(?)"
    TSM "“Shit, [player_sb] [player_gender] not back?“"
    MC "(OH shit)"
    scene inside with fade
    show tsm nsilent
    MC "“No, I’m here! Sorry, I was catching up on my homework.“"
    show tsm nnormal
    TSM "“Oh, okay."
    TSM "“I’ll get started with dinner then.“"
    hide tsm
    "He places all of his bags on the floor before grabbing the maid outfit from the hanging rack and heading over to the bathroom to change into it."
    MC "(I don’t think I’ve ever really enforced the maid outfit thing ever since I gave it to him on the first day. So it’s kind of a miracle that he’s wearing it now with no complaints.)"
    MC "(I kinda thought he would pretend to forget. Especially when i’m so focused on my stuff that I barely notice my surroundings.)"
    MC "(But no, he really stuck to it. He’s just obediently listened to me without much protest.)"
    MC "(On day 3 I ended up buying a second identical set just so he won’t have to wear the same one everyday.)"
    MC "(He looks cute in it though.)"
    show tsm mangy
    TSM "“You’re smiling.“"
    show tsm mpout
    MC "“I can’t smile now?“"
    show tsm mangy
    TSM "“It’s the evil smile. It’s your grin.“"
    show tsm munsure
    TSM "“What are you up to?“"
    show tsm msilent
    MC "“I’m not up to anything!“"
    MC "(Well, nothing bad.)"
    show tsm munsure
    TSM "“Uh huh, that’s not very convincing...“"
    show tsm mnormal
    TSM "“I’m just gonna go cook dinner. You still have homework to finish, yea?“"
    MC "“Yep!“"
    
    scene cg1 with fade
    MC "(I know I said I was gonna do my homework. But DAMN, having a cute boy in maid outfit is really distracting.)"
    MC "(There’s something special about seeing him with the cute little frilly headwear, the bows and ruffles, and the way the skirt beautiful swishes around and you can see the layers and lace underneath.)"
    MC "(All this combined with his little ponytail and pouty expression. Makes him look real kissable.)"
    MC "(Wait...kissable? Do I like him now...?)"
    MC "(Did I like him even before this...?)"
    scene cg1 with vpunch
    MC "(WAIT.)"
    MC "(THAT DREAM I HAD OF HIM THE NIGHT I OFFERED TO LET HIM STAY WITH ME!!!!)"
    MC "(MAYBE I DO LIKE HIM.)"
    MC "(I feel like I should’ve realized this a week ago, but oh well.)"
    TSM "“[MC]! Dinner’s almost done.“"
    MC "“Got it!“"
    
    scene insidepd with fade
    "Upon hearing his voice I got up from my seat and started setting up the plates and utensils."
    "Ever since our last time eating, I’ve officially bought that picnic blanket for us to eat on."
    "It’s kind of nice since it brings a little whimsy into my life."
    show tsm mnormal:
                   parallel:
                           ease .5 zoom 1.3
                   parallel:
                           yalign 0.0
                           linear 0.0 yalign 0.0 xalign 0.5
    TSM "“Here, eat up.“"
    show tsm msilent
    MC "“Oh? We got kind of fancy today. There’s an extra side dish.“"
    show tsm mnormal
    TSM "“We had extra ingredients.“"
    show tsm msilent
    MC "“And here I thought you wanted to celebrate our first week together.“"
    show tsm mbsurprised
    TSM "(!!)"
    MC "“Am I spot on?“"
    show tsm mbangy
    TSM "“No dumbass. That’s not it.“"
    show tsm mdeflecting
    TSM "“A-and stop looking at me like that.“"
    MC "(Oh. OH. I feel like I should’ve noticed this last week too but does he..also, maybe, kinda, like me too??)"
    MC "(Is this a sign for me to make a move?)"
    show tsm mpout
    MC "“Are you sure?“"
    show tsm mstopit
    TSM "“Yes! Now, can we eat? Or do you have anything better to eat?“"
    MC "“Of course not, you’re the best as far as I’m concerned.“"
    show tsm mangy
    TSM "“Geez, save that kind of flattery for your boyfriend dammit.“"
    show tsm msilent
    MC "“Huh?“"
    show tsm munsure
    TSM "“Your boyfriend. The one with white hair?“"
    show tsm mnormal
    TSM "“I saw you two earlier, you don’t need to eat my food if you have him to cook for you.“"
    MC "“That’s not my boyfriend.“"
    show tsm munsure
    "Upon hearing that, he stops eating and looks at me questioningly, almost suspiciously."
    TSM "“Then who the fuck was the guy glaring at me at campus?“"
    show tsm msilent
    MC "“Who?“"
    show tsm mnormal
    TSM "“Y’know, the one walking next to you this afternoon.“"
    show tsm msilent
    MC "“OH! So that was you!“"
    MC "“I waved at you but you ran away!“"
    show tsm mangry
    TSM "“Your boyfriend was glaring at me! And I've never met him!“"
    show tsm msilent
    MC "“Again, not my boyfriend.“"
    MC "(Notice that I’m into you dammit.)"
    show tsm mnormal
    TSM "“But...you were so close?“"
    TSM "“He was offering to cook for you and everything.“"
    show tsm msilent
    MC "“Nix? He’s just my friend. Hell if I know why he offered, I turned it down anyway.“"
    show tsm msmirk
    TSM "“You turned down free food? Sounds unlikely.“"
    MC "“Yes? I have your cooking and I really like it, better than anything else I’ve ever had...“"
    MC "“Especially tonight.“"
    show tsm munsure
    TSM "“Huh?“"
    show tsm msure
    TSM "“I mean, thanks?“"
    show tsm msilent
    MC "“How did you get so good at this anyway?  I know the answer is just by cooking a lot, but how?“"
    MC "“Personally, I feel like I'm always too tired to cook.“"
    show tsm mnormal
    TSM "“I dunno, I just happened to learn it.“"
    TSM "“I see food and I think, 'That looks overpriced, bet I can do better'.“"
    TSM "“And then I made it.“"
    MC "“And is it actually better?“"
    show tsm msmirk
    TSM "Dunno, you tell me."
    menu:
        "I guess it is.":
                show tsm mhappy
                TSM "“There you go then.“"
        "It’d be even better if I can have the chef for dessert.":
                show tsm mbsurprised
                TSM "(!!)"
                MC "(That’s not a bad reaction, I think. Maybe I can push further.)"
                show tsm mbsdquestioning
                TSM "“H-hey quit it. I’m not on the menu.“"
                MC "“I can’t get a chef’s kiss?“"
                show tsm mbstopit
                TSM "“N-no dumbass. Go eat in peace.“"
                MC "“Finee.“"

    show tsm munsure
    TSM "“Sometimes I wonder if you have a few screws loose.“"
    show tsm msilent
    MC "“I’ll have you know that I’m perfectly sane.“"
    show tsm mnormal
    TSM "“What sane person invites a neighbor they barely know to live with them for a month?“"
    show tsm msilent
    MC "“Me. I’m a sane person.“"
    show tsm msmirk
    TSM "“I highly doubt that.“"
    show tsm msilent
    MC "“‘Sides you’re not a ‘neighbor I barely know’, you’re a friend. A pretty good one too.“"
    MC "(And also a pretty one.)"
    show tsm mnormal
    TSM "“You consider me a friend?“"
    MC "“You don’t?"
    show tsm msdnormal
    TSM "“I-uh...“"
    TSM "“I didn’t think I was that important.“"
    show tsm mnormal
    TSM "“And it’s not like we’ll be interacting with each other for long, after the semester is over we’ll move to different places.“"
    TSM "“Then you won’t have a reason to talk to me.“"
    show tsm msilent
    MC "“I’ll just have to find one then. I have your contact number.“"
    show tsm msdnormal
    TSM "“Then what? You don’t really have much to talk about with me.“"
    TSM "“We’re not in the same major or anything so you’re not gonna ask me about homework.“"
    TSM "“We don’t share club activities either.“"
    show tsm msilent
    MC "“Wouldn’t that give us more things to talk about though?“"
    MC "“Since you don’t know my activities, and I don’t know yours, we can just swap stories about those!“"
    MC "“And you can always text me if you have a game coming up, I’ll try to cheer you on if I’m not busy!“"
    show tsm msure
    TSM "“I guess...“"
    show tsm munsure
    TSM "“But are you really gonna do that...?“"
    menu : 
        "Maybe not, but we might see each other around campus?":
                MC "“Our schedules will change depending on our classes next semester, it might line up next time?“"
                show tsm mnormal
                TSM "“I doubt that.“"
        "I don’t see a reason not to.":
                MC "“I like being around you, and I can only hope that you do too?“"
                show tsm mbsure
                TSM "“I-I...“"
                show tsm msdnormal
                TSM "“Well..uh..you’re not that bad to be around I guess.“"
                MC "“Is it that hard to admit that you like me?“"
                show tsm mbstopit
                TSM "“I don’t!“"

    show tsm mnormal
    TSM "“Anyway, you done eating? I’m gonna clear the plates.“"
    show tsm mbsurprised
    MC "“Wait! It’s time for dessert!“"
    "He makes an undignified yelp, and stares at me like a deer caught in headlights."
    show tsm mdeflecting
    TSM "“HUH?! Y-you can’t seriously be...!“"
    MC "“What’s wrong?“"
    MC "(I was gonna bring out the puddings, but I’m guessing he thinks I want {i}him{/i} for dessert?)"
    MC "(Aww, that’s too cute.)"
    show tsm mbsdquestioning:
                   parallel:
                           ease .5 zoom 1.5
                   parallel:
                           yalign 0.0
                           linear 0.0 yalign 0.0 xalign 0.5
    "I lean closer towards him and he freezes on the spot, eyes looking in a million different directions besides my face."
    show tsm mbsdquestioning with vpunch
    TSM "“W-we can’t! You...a-and...me...we’re not...like...a-and the walls...“"
    MC "“But I want dessert, don’t you?“"
    show tsm deflecting
    TSM "“You gotta be joking..! W-with me?“"
    MC "“Yes with you, who else?“"
    TSM "“I-I don't know-“"
    TSM "“Urgh...“"
    show tsm bstopit
    TSM "“I..uh....fine.“"
    show tsm mbsdquestioning
    TSM "“Do what you want with me... Just be quick.“"
    show tsm mbpout
    "He seemingly steels his nerves, finally staring right at me despite the red flush on his cheeks."
    "His eyes glisten with anticipation on my next move, his breathing speeding up."
    MC "(OH. That’s kinda hot.)"
    show tsm mbangy
    TSM "“So? Get on with it.“"
    show tsm mbpout
    MC "“Good boy, wait here.“"
    "(I feel a little bad that I left him there without clearing up his misunderstanding, but seeing him like that is way too fun.)"
    
    scene insidepd with fade
    "Soon enough, I returned back with the puddings in my hands."
    MC "“Ta da! Dessert!“"
    show tsm munsure
    TSM "“Huh...?“"
    MC "“Dessert, I bought you pudding!“"
    "Feigning innocence, I give him my most angelic smile (Or at least I tried, I’ve never been good at smiling like that)."
    show tsm mangy
    TSM "“So you weren’t talking about...?“"
    MC "“About what?“"
    "I tilt my head to feign confusion, trying my best to not slip up on the act."
    show tsm mdeflecting
    TSM "“Y-you...“"
    show tsm mpout
    MC "“Not sure what you thought I was talking about, but I figured I’d buy you pudding to celebrate your first week surviving here.“"
    MC "“And as a peace offering for whatever I’ve done that you may not like.“"
    show tsm mhappy
    "Despite seeming a little disappointed at first, his expression shifts to one of unexpected joy."
    show tsm msure
    TSM "“You bought this for me?“"
    MC "“Well the other one’s mine but if you’re that hungry then you can eat both.“"
    show tsm msmirk
    TSM "“I’m not that greedy, stupid.“"
    show tsm msure
    TSM "“And um, thanks. I love pudding.“"
    TSM "“How did you know I liked this?“"
    show tsm msilent
    MC "“Because you told me? I’ve been collecting information about you through our dinner conversations.“"
    MC "“Pretty sure I asked you this question 3 days ago.“"
    show tsm mhappy
    TSM "“Thanks, I guess we both have somethin’ special for today huh?“"
    MC "“And here I thought we just had 'extra ingredients'.“"
    show tsm mbsurprised
    TSM "(!)"
    show tsm msdnormal
    TSM "“Don’t read into it. We did, but I also felt like making something else.“"
    show tsm msilent
    MC "(Aww, I think he’s starting to warm up to me.)"
    MC "“I’m glad you did. How’s the pudding?“"
    show tsm mhappy
    TSM "“Great! This didn’t cost you too much, right?“"
    MC "“Oh it was a million bucks.“"
    show tsm msmirk
    TSM "“Shut the fuck up, no it wasn’t.“"
    show tsm msilent
    MC "“I know, just messin’ with ya.“"
    show tsm mhappy
    TSM "“I’m starting to think you do certain things just to mess with me.“"
    show tsm msilent
    MC "“Sorry, do you hate it?“"
    show tsm mhappy
    TSM "“Too late for that, you’ve already shoved me into this maid outfit.“"
    show tsm msilent
    MC "(He’s not necessarily saying that he hated it though.)"
    show tsm mdeflecting
    MC "“Hey, I didn’t ‘shove’ you into it, I just gave it to you and you wore it.“"
    MC "“It’s not like I was helping you change.“"
    show tsm mangy
    TSM "“A-are you done? I’m gonna clean up and study.“"
    show tsm mpout
    MC "“You’re not saying that you hate it though.“"
    show tsm mdeflecting
    TSM "“I’m gonna clean up-!“"
    show tsm mpout
    MC "“Alright, I’ll help you.“"
    "(And so ends the night of our one week of living together.)"
    
    scene insiden with fade
    MC "(...)"
    MC "“Rudy?“"
    show tsm snormal
    TSM "“Yea?“"
    show tsm ssilent
    MC "“G’night.“"
    show tsm snormal
    TSM "“G'night to you too.“"
    show tsm ssilent
    TSM "..."
    show tsm suhsure
    TSM "“That all?“"
    show tsm ssilent
    MC "“Oh I also wanted to say that I love you.“"
    show tsm ssmirk
    TSM "“Quit messin’ with me and go to bed dumbass.“"
    show tsm ssilent
    MC "“m’not though.“"
    show tsm snormal
    TSM "“You’re tired, go to bed.“"
    show tsm ssilent
    MC "“Fine.“"
    
    scene black with fade
    MC "..."
    scene kosdream with fade
    play music "audio/ed6.mp3" fadein 1.0 
    #yg buat mimpi bgm yg music box ini
    MC "(Shit, am I late?)"
    "I pull out my phone to check the time, it seems like I still have plenty to spare."
    MC "(That’s good, wouldn't wanna be late this early in the semester.)"
    MC"(Hm?)"
    MC "(What’s that smell? It’s delicious.)"
    MC "(Warm rice...Crispy Sides...Nice Sauce...)"
    MC "(Hmmm, something smells good.)"
    MC "(I still have time right? I wanna check out the source.)"
    MC "(Shit, I’m getting hungry...)"
    show tsm nsurprised with vpunch
    GTWU "(!!!)"
    GTWU "“Shit, you came out of nowhere.“"
    show tsm nsilent
    MC "“Sorry! My bad for bumping into you.“"
    show tsm nnormal
    GTWU "“It’s fine.“"
    show tsm nsilent
    MC "(Actually, I feel like the smells coming from him.)"
    MC "(Shit, he smells delicious!)"
    show tsm nuhsure
    GTWU "“Uhh, did you hit your head or something?“"
    MC "“You smell good“."
    show tsm nhuh
    MC "(Maybe I shouldn’t’ve said that.)"
    GTWU "“Wha? Don’t sniff me jackass.“"
    show tsm mnsilent
    MC "“My bad, you smell like food. Where did you buy it?“"
    show tsm nnormal
    GTWU "“I didn’t buy it, I made it myself.“"
    GTWU "“I’m not feeding you shit.“"
    show tsm nsilent
    MC "“Wasn’t expecting you to. I already had breakfast.“"
    show tsm nuhsure
    GTWU "“And you’re still eyeing me like that?“"
    show tsm nnormal
    GTWU "“Whatever, I gotta go. I have this campus event in a bit so, sort that shit yourself.“"
    show tsm nssilent
    MC "“Wait a sec, you go to Begonia’s Institute of Technology too?“"
    show tsm nhuh
    GTWU "“Shit, you too?“"
    MC "“Yea! Wanna walk together?“"
    show tsm nnormal
    GTWU "“No.“"
    show tsm nsilent
    MC "“C’mon, help me out here. What if I get lost?“"
    show tsm nnormal
    GTWU "“That’s your problem.“"
    show tsm nsilent
    MC "“What if you get lost?“"
    show tsm nnormal
    GTWU "“Then that’s not your business.“"
    show tsm nsilent
    MC "“I can help you out? Two heads are better than one.“"
    show tsm nuhsure
    GTWU "“You’re awfully chummy to someone you just met.“"
    show tsm nsilent
    MC "“Sorry, I got a bit lonely since all my friends went to different colleges and I haven’t met anyone here.“"
    MC "“You’re actually the first one I’ve seen!“"
    show tsm nuhsure
    GTWU "“Is that supposed to be some kinda honor?“"
    show tsm nsilent
    MC "“Nope! I just wanted to talk to someone.“"
    show tsm nuhsure
    GTWU "“Guess I have no choice, huh?“"
    show tsm nsilent
    MC "“Well, you can always just run away from me? I don’t mind.“"
    show tsm nhappy
    GTWU "“Whatever."
    GTWU "“So, are you coming or not?“"
    show tsm nsilent
    MC "“I am!"
    MC "“Actually, I don't know your name yet!“"
    show tsm nnormal
    TSM "“Rudy."
    MC "“Nice to meet you ! I’m [MC].“"
    show tsm nhappy
    TSM "“Alright.“"

label week_ym:
    #YM Maid Week Later"
    scene insidepd with fade
    MC "(And so, my first week with Nix passes.)"
    MC "(I don’t know what I was expecting when I first agreed but in some ways he did improve my life.)"
    MC "(Mostly surrounding cooking and other housework, if nothing else my place is the cleanest it’s been in weeks.)"
    if YM_dp >= 5:
        MC "(Honestly though, I can’t wait for the month to be over.)"
        MC "(Shit thing to say about living with your friend but I don’t know, the more I know about him the more I sense the bad vibes.)"
        
    else:
        MC "(It’s been pretty good, although I do think he’s been too much recently.)"
        MC "(WAY above ‘friend’ level.)"
    
    MC "(Regardless, I’ve decided to be nice and buy something to celebrate.)"
    MC "(And as a sort of thanks for all he’s done for me this past week.)"
    MC "(Based on what I know about him, he seems to like those cookies with the strawberry jam so I’ll buy those.)"
    MC "(Trying to make those myself would be disastrous.)"
    show ym nnormal
    YM "“What are you thinking about [MC]? You seem distracted today.“"
    show ym nsmile
    MC "“I’m good.“"
    show ym nhappy
    YM "“Really? You can always tell me if something is wrong. If nothing else, I can always act as a stress reliever.“"
    show ym nsmile
    MC "“That won’t be necessary.“"
    show ym nhappy
    YM "“Are you sure? I can skIp my morning class and stay here with you.“"
    show ym nworry
    MC "“No way man, go to class.“"
    MC "“I’d hate to ruin your perfect attendance.“"
    show ym nwhine
    YM "“But...“"
    MC "“No buts! Go to class.“"
    show ym nworry
    YM "“Fine...“"
    show ym napologetic
    YM "“Do I get anything for being a good boy?“"
    MC "“Yes, you get to keep your perfect attendance.“"
    show ym nhuffy
    YM "“Booo...!“"
    show ym nhuffy
    MC "“Enough pouting, go already. Wouldn’t want you to be late.“"
    show ym nhappy
    YM "“Can I atleast get a goodbye hug?“"
    menu:
        "Sure why not?":
                show ym nrhappy: 
                        parallel:
                            ease .5 zoom 1.5
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.0 xalign 0.5
                "He beams with joy and soon buries himself in my chest, seeming way too comfortable, like he’s never gonna let go."
                show ym napologetic
                YM "“You’re the best, [MC]...“"
                MC "“I know, but you should go now.“"
                show ym nhappy
                YM "“Alrightttt.“"
        "No, just go already.":
                $ YM_dp +=2
                show ym nmtch
                YM "{size=-10}“Shit.“{/size}"
                MC "“What was that?“"
                show ym nhappy
                YM "“Nothing!“"
                show ym rhappy
                YM "“Okie then, byee!“"
                MC "“Bye!“"
                hide ym
                if dp >= 4:
                    "Once he leaves, I breathe a sigh of relief."
                    MC "(I’m starting to hate him, immensely.)"
                else:
                    "When he eventually gets further away, I shut the door and find a smile creeping on my face."
                    MC "(He’s pretty cute when he’s like that.)"
    
    scene campus1d with fade
    MC "(I’m glad I managed to buy those cookies before I have class.)"
    MC "(I just know Nix would sniff me out if I bought it later.)"
    MC "(Is that...?)"
    show tsm nsilent
    MC "(Rudy?)"
    MC "(Man, I’ve been seeing him more often lately. It went from once every few months to once a week.)"
    MC "(No where near how often I encounter Nix though, so seeing him is a good change of pace.)"
    MC "“Rudy what’s up!“"
    show tsm nhuh
    TSM "“Huh?“"
    "He faces my direction, a little confused. I give him a wave as I approach him and he returns the gesture."
    show tsm nsilent
    MC "“What’s up? I don’t usually see you around."
    show tsm nnormal
    TSM "“Same here, you followin me around or somethin'?“"
    show tsm nsilent
    MC "“Obviously not, I don’t have the time for that.“"
    show tsm nhappy
    TSM "“I sure hope so.“"
    show tsm nsilent
    MC "“You seem on edge, life treating you badly?“"
    show tsm nnormal
    TSM "“Nothing I can't handle.“"
    show tsm nsilent
    MC "“Well that’s good.“"
    show tsm nsdquestioning
    TSM "“Umm...I’ve got somethin to ask.“"
    show tsm nsilent
    MC "“Shoot“"
    show tsm nunsure
    TSM "“Did your friend move to our place? I’ve been seeing him around our place a lot.“"
    show tsm nsilent
    MC "“Yea, he did.“"
    show tsm nnormal
    TSM "“Why? Kinda strange to move in just before the semester’s over.“"
    show tsm nunsure
    TSM "“He’s not stalking you or anything, is he?“"
    show tsm nsilent
    MC "“Nah (probably). Remember the fire?“"
    show tsm nnormal
    TSM "“Oh, that.“"
    show tsm nuhsure
    TSM "“That was his room?“"
    show tsm nsilent
    MC "“Uh no, his room is unscathed but he got scared and asked to move in with me.“"
    show tsm nhuh
    TSM "“You’re living together?!!??“"
    show tsm nuhsure
    TSM "“Are you two...dating?“"
    show tsm nsilent
    MC "“Well-“"
    show ym nrhappy at right:
        linear 0.050 xoffset -10
        linear 0.050 xoffset +0
        linear 0.050 yoffset -10
        linear 0.050 yoffset +0
    show tsm nsilent at left
    YM "“[MC]!“"
    
    "Suddenly, I was tackled into a hug by an overly excited Nix. Once he releases me from the hug, he continues his hugging spree and staked his claim on my arm."
    show ym nquestioning
    YM "“[MC], who is this?“"
    MC "“That’s our downstairs neighbor.“"
    show ym ngrin
    YM "“Nice to meet you. I’m Nix.“"
    "He smiles as sweetly as he always does, but this time the light doesn’t quite seem to reach his eyes."
    show tsm nsdquestioning
    TSM "“Uh yea, sure.“"
    show tsm nangry:
        linear 0.050 xoffset +10
    "Like a cat sensing a threat, Rudy seems to instinctively back away from Nix, not bothering to hide his less than thrilled expression."
    MC "(I guess he is kinda bad with strangers.)"
    show ym nnormal
    YM "“What are you talking about with my [player_pronoun]?“"
    show ym nsilent
    show tsm nsdanrgy
    TSM "“Nothing, I’m about to leave anyway.“"
    TSM "“So I guess he is your boyfriend?“"
    menu:
        "Nix, quit messing around. We’re not together.":
                $ YM_dp +=2
                $ YM_ij +=1
                show ym nworry        
                YM "“[MC]...Don’t be like that, am I not enough for you? I can change...“"
                MC "“That’s not the issue here.“"
                YM "“But, [MC]...“"
                "I yank my arm out of his embrace and he stumbles back from the force."
                MC "“Don’t.“"
                show ym nwhine
                YM "“[MC]...!“"
                show tsm sdangy
                TSM "“Hey, if [MC] isn’t interested then fuck off.“"
                show tsm nserious
                show ym nmnormal
                YM "“Don’t put your words into [MC]’s mouth.“"
                show ym napologetic
                YM "“[MC]...won’t you tell him to back off?“"
                MC "“Well, he’s not wrong. I’m not exactly-“"
                show ym nwhine
                YM "“[MC]!“"
                show tsm ndeflecting
                "As Nix approaches me once more, Rudy quickly moves in front of me to strike a hit."
                play sound "audio/punch.mp3"
                show ym nblnose
                TSM "“Shit, I’m sorry!“"
                show tsm nserious at center
                hide ym        
                "Not wanting to deal with Nix at the moment, I hurriedly follow behind Rudy as he runs away from the scene of the crime. "
                "Once in a while, Rudy would look behind to see if I’m still there."
                "Pretty sure we got a few odd looks, but by this point the adrenaline is getting to me."
                scene campusd with fade
                "By the time we reached somewhere more secluded I was tired as all hell."
                TSM "“Are you okay?“"
                MC "“I’ll live.“"
                TSM "“What’s up with him?“"
                MC "“I don't know, I’ve never seen him like this.“"
                
                if dp == 10: 
                    TSM "“And you’re telling me you live with him?“"
                    TSM "“If you feel uncomfortable then kick him out! It’s not like he’ll go homeless if you do.“"
                    MC "“His things are in my room, I have class in 10 minutes and his finishes before mine.“"
                    MC "“It'll be harder to kick him out if all his belongings are with me.“"
                    "Rudy gives me a sigh before looking back at me."
                    TSM "“Tell you what, I’ll get rid of his things for you.“"
                    MC "“You’d do that for me? Don’t you have class?“"
                    TSM "“It starts in 2 hours, I’ll be fine.“"
                    MC "“Why go this far for me?“"
                    TSM "“It’s not for you. {b}I{/b} feel unsafe knowing he’s around.“"
                    MC "“He lives across the street though.“"
                    TSM "“FUCK.“"
                    TSM "“Y’know what, fuck that. That’s a problem for later. For now, we gotta get him outta our place.“"
                    TSM "“What do I need to get?“"
                    MC "“Well...“"
                    scene campus with fade
                    MC "“That’s about it.“"
                    TSM "“If I remember correctly, our rooms have the same layout right?“"
                    MC "“Yep."
                    TSM "“Cool, I’ll try to help you out.“"
                    MC "“Thanks a lot man! You’re a lifesaver.“"
                    TSM "“Shut up, don’t make a big deal out of it.“"
                    TSM "“See ya’“"
                    MC "“Byee! And thanks!“"
                    MC "(Alright, time to get to class.)"
                
                else:
                    MC "“But he’s not usually like this.“"
                    TSM "“Do you want him out?“"
                    MC "“No, he’s my friend and he’ll be out in a month anyway. He’s just staying with me because he’s afraid of another fire.“"
                    TSM "“If you say so.“"
                    TSM "“You sure you’re okay?“"
                    MC "“Yea, I’m sure.“"
                    TSM "“Okay then, need me to walk you to your building? Just in case he’s after you.“"
                    TSM "“I’m sure taking down someone would be easier with 2 people.“"
                    MC "“Sure, although...“"
                    MC "“Nix isn’t particularly strong.“"
                    TSM "“Wouldn't hurt to be safe though.“"
                    MC "“Alright, thanks for offering.“"

        "Clingy isn’t he? Not that I mind.":
                show ym nrhappy
                YM "“Hehe.“"
                show tsm nnormal
                TSM "“Uh huh, whatever.“"
                TSM "“See you some other time.“"
                hide tsm
                show ym nnormal at center
                YM "“Why were you talking to him, [MC]?“"
                MC "“Because I saw him and I figured I’d say hi?“"
                show ym nhuffy
                YM "“Don’t...“"
                MC "“Why?“"
                show ym nmnormal
                YM "“Because you’re with {b}me{/b}.“"
                MC "“Uh Nix? You’re holding on a bit too tight there.“"
                show ym napologetic
                YM "“Oh! Sorry, is this better?“"
                MC "“Yea."
                show ym nhappy
                YM "“Alright then, shall we go to class?“"
                MC "“Sure.“"

    scene road with fade
    MC "(Class is done!)"
    MC "(Time to get back to my place and see Nix again.)"
    if  YM_ij == 1 and YM_dp <= 9:
        MC "(And maybe check on that bloody nose of his since I do feel a little bad.)"
        MC "(Just a little.)"
    else: 
        MC "(And give him those cookies I got to mark his first week here.)"
        MC "(Might as well show a little appreciation for him.)"
        
    
    if dp == 10:
        MC "(Dear lord, class is officially over.)"
        MC "(I genuinely don’t wanna deal with Nix while I’m this tired but what else can I do?)"
        MC "(I’m just glad Rudy was there to help.)"
        MC "(Whatever, I’ll think about this when I get there.)"
        scene black with fade
        #stop bg music
        play sound "audio/creakyed1.mp3"
        MC "“Nix? I’m back.“"
        MC "(It’s so dark, what is he even doing like this?)"
        scene insiden with fade
        MC "Nix?"
        show ym siluet with vpunch:
                    parallel:
                        ease .5 zoom 1.7
                    parallel:
                        yalign 0.0
                        linear 0.0 yalign 0.0 xalign 0.0
        play sound "audio/spray.mp3"
        MC "“FUCK!!“"
        play sound "audio/punch.mp3"
        scene black
        play sound "audio/fabric.mp3"
        YM "“Sorry, [MC]. Forgive me alright?“"
        MC "(My head hurts, what the fuck happened?)"
        MC "(Shit, I’m losing consciousness...)"
        YM "{size=-5} “I’m sorry, I’m sorry, I’m sorry,I'm sorry I'm sorry I'm sorry im sorry im sorry“{/size}"
        MC "(?)"
        YM "{size=-10} I’m sorry, I’m sorry, I’m sorry,I'm sorry I'm sorry I'm sorry im sorryim sorry“{/size}"
        "..."
        pause
        
        GTWU "“Hmm hm hmm hm~“"
        MC "(?)"
        GTWU "“Hmm hm hm hmm~“"
        scene insiden with fade
        MC "(My head hurts...)"
        YM "“[MC]! You’re awake.“"
        MC "(Is that...Nix? Still in the maid outfit...)"
        #make the outfit bloody"
        show ym ed1sorry
        YM "“Oh, please don’t struggle too much. You’ll hurt yourself.“"
        YM "“I try to get up from my position, but fail.“"
        YM "“As my consciousness returns, I realize that I’ve been buried under blankets and duct taped to my bed.“"
        YM "“When I struggle once more to get up, Nix quickly panics and frantically places himself on top of me, acting as an extra weight.“"
        show ed1ver2 with fade
        $ persistent.ed1ver2_unlocked = True
        YM "“Please don’t do this to me, [MC]...Stay with me...“"
        YM "“I don’t wanna hurt you more than I have...“"
        MC "“The fuck?“"
        YM "“I’m sorry I have to do this [MC], but i’m scared you might leave me. And I can't let that happen.“"
        YM "“After all, I’ve worked so hard for this. I worked so hard for {I}you{/I}.“"
        MC "(Why...? I thought Rudy was supposed to kick him out.)"
        MC "(Did he bail on me?)"
        YM "“Oh [MC], don’t look away from me. Keep your eyes on me and me alone.“"
        YM "“Don’t think for one second that I didn't know what he was about to do.“"
        MC "“What happened to Rudy?“"
        YM "{b} “Don’t even say his name!“{/b}"
        YM "“Woops, sorry for raising my voice at you. Please don’t do it again [MC], you know that it upsets me.“"
        MC "{b}“What happened?“{/b}"
        YM "{b}“I SAID DON’T MENTION HIM“{/b}"
        YM "“What do I need to do to get your mind off of him [MC]? Please tell me, I’ll do anything.“"
        MC "“Tell me. What. Happened. To. Rudy.“"
        YM "“ARRGHHH, Must you be so {b}stubborn{/b}!“"
        YM "“You don’t need to know anything. All you need to know is that he won’t come between us anYMore, so don’t worry.“"
        YM "“I took care of everything, so please don’t even think about him anymore.“"
        YM "“He’s in your past, [MC].“"
        MC "“What did you do?!“"
        YM "“STOP...!!!“"
        "Something seems to snap even further in Nix as heavy tears start streaming down his face.“"
        YM "“PLEASE..JUST…LOOK AT {b}ME{/b}“"
        show ed1ver1
        $ persistent.ed1ver1_unlocked = True
        YM "“He’s dead, okay???! DEAD! He’s gone and all you have left is {b}me{/b}.“"
        MC "“You’re fucking lying.“"
        YM "“See [MC], I’m stronger...! All I needed to do was continuously spray his face with mosquito repellent before stabbing him..!“"
        MC "(Guess that’s why the room smells like this.)"
        YM "“Why can’t you please see who it is that truly wants you? It’s me.“"
        MC "“Want me? Or want me dead?“"
        YM "“I wouldn’t do that..! I love you [MC], always have and always will.“"
        YM "“Please...You have to believe me. You’re the only reason why I even chose this college.“"
        YM "“You’re the only reason why I chose my current place.“"
        YM "“All this is so that I could be close to you...!“"
        YM "“And you still won’t even consider me!“"
        MC "“If there’s 7 billion people in this world, I’m not going for you.“"
        YM "“Why won’t you just understand?“"
        YM "“I love you.“"
        YM "..."
        YM "“I know what to do...“"
        YM "“I think I need to prove it to you. Then you’ll believe me, right?“"
        "In an instant, he closes the distance between us and places his lips on mine. His hands desperately cupping my face while his tears fall down onto mine.“"
        "I try to get him off but he moves his other hand to hold me down to the bed.“"
        YM "“Do you get it now, [MC]?“"
        YM "“You’re mine you’re mine you’re mine you’re mine you’remine youremine youremine youremine youremine youremine“"
        MC "(Fuck, I should’ve known that I would attract someone crazy.)"
        "Ending 1 : You’re Mine."
        return
        
    else:
        scene inside with fade
        MC "“Nix? I’m back.“"
        show ym mrhappy
        YM "“Welcome back, [MC]!“"
        
        if YM_ij == 1:
            MC "“How’s your...uhh...face? I have an ice pack around here somewhere.“"
            show ym mconcerned
            YM "“[MC]...It hurts...“"
            MC "“Sorry. I’ll make it up to you now.“"
            show ym nworry
            YM "“That guy you were with, I don’t like him...“"
            MC "“Again, sorry about that. I think he was just trying to help me out.“"
            MC "“I don’t appreciate you telling other people lies like that, y’know?“"
            show ym mhuffy
            YM "“Hmph...fine...“"
            MC "“Here, give me your hand.“"
            show ym mwhine
            YM "“It’s colddd..!“"
            MC "“It’s an ice pack, hold it up to where Rudy punched you earlier.“"
            show ym mnormal
            YM "“Okayyy.“"
        
        else:
            show ym msmile
            MC "“So...boyfriend, huh?“"
            show ym mapologetic
            YM "“Umm...sorry about that. You don’t mind, do you, [MC]?“"
            show ym mworry
            YM "“I just felt this tightness in my chest when I saw you with him..and I don’t know what to do about it...“"
            MC "“So you got jealous?“"
            show ym mconcerned
            YM "“Please don’t hate me...“"
            MC "“Chill, I don’t.“"
            show ym mapologetic
            YM "“That’s good.“"

    show ym mrhappy
    YM "“Anyway, I already made dinner!“"
    MC "“Already? I haven’t even set up our picnic blanket yet.“"
    show ym mhappy
    YM "“It’s okay, I still need to grab the food from the kitchen.“"
    show ym msmile
    MC "“Gotcha’, I’ll set it up for us while you do that.“"
    scene insidepd with fade

    show ym mhappy    
    YM "“[MC], you done?“"
    show ym msmile
    MC "“I am, let’s dig in.“"
    show ym mrhappy
    YM "“Okie, here you go!“"
    show ym msmile:
        parallel:
            ease .5 zoom 1.5
        parallel:
            yalign 0.0
            linear 0.0 yalign 0.0 xalign 0.5
    MC "“Y’know, I’m sorry for ever doubting you, I guess you are good at this!“"
    show ym mapologetic
    YM "“I’m glad you think so but...“"
    show ym mmad
    YM "{b}“Am I even better than the guy downstairs?“{/b}"
    MC "“Huh?“"
    show ym mnormal
    YM "“I heard that he’s a good cook. I heard that you asked to taste his lunch at some point.“"
    MC "(Where is this coming from?)"
    MC "“I wouldn’t know, I never got a taste of his cooking.“"
    show ym mmad
    YM "“I saw you walking to campus with him a week ago, why did you meet up with him?“"
    MC "“I didn’t ‘meet up’ with him, I didn't plan anything.“"
    MC "“I saw my neighbour and figured we’d have a chat since we’re heading in the same direction.“"
    MC "(Why is he making such a big deal out of me and my neighbor walking together? I haven’t even seen him in months at that point!)"
    MC "“How do you even know that? You weren’t there.“"
    show ym mworry
    YM "“And you were with him again this afternoon...“"
    show ym mwhine
    YM "“You should’ve called me. I’m the one who’s closer to you!“"
    MC "“For what? I’m just walking to class, we’re not hanging out or anything.“"
    YM "“Still-! Y-y...you-“"
    show ym mmcangry:
        parallel:
            ease .5 zoom 2.0
        parallel:
            yalign 0.0
            linear 0.0 yalign 0.0 xalign 0.5
    YM "{b}“You’re mine!“{/b}"
    MC "(...)"
    show ym mhorrified:
        parallel:
            ease .5 zoom 1.5
        parallel:
            yalign 0.0
            linear 0.0 yalign 0.0 xalign 0.5
    "Realizing his sudden outburst, he clams up and falls to his knees, seemingly horrified for raising his voice at me."
    MC "(This is the first time I’ve seen him this upset over anything.)"
    MC "(Scratch that, this is the first time I've seen him upset in general.)"
    MC "“Nix?“"
    show ym mwhine
    YM "“S-sorry, I-I don’t know what came over me...“"
    menu:
        "Are you okay? You seem on edge.":
                show ym mconcerned
                YM "“I-I’m sorry, I shouldn’t’ve yelled like that.“"
        "You better be, You don’t get to be mad over who I interact with.":
                show ym mwhinecry
                YM "“I’M SORRY-! Y-you probably hate me now d-don’t you?“"
                    
    MC "“I hate to say this but you’ve been a bit weird for a while now. What's up?“"
    show ym mworry
    YM "“[MC]...I...I...“"
    "He struggles to get the words out before suddenly snapping back to normal, if a little more unhinged than usual."
    #ganti bgm sini
    show ym mgrin
    YM "“Nothing’s wrong, [MC]!“"
    YM "“I’ve just been a little tired, maybe it’ll all be better if you let me cuddle up to you after this?“"
    YM "“After all, I did do allll of this just for you.“"
    MC "“Why? Why go this far for me of all people? You're not acting like yourself.“"
    show ym mquestioning
    YM "“Why not? As far as I’m concerned you’re the only important person in the world.“"
    MC "“C’mon be real with me here. You’re pretty friendly, and you have lots of friends. Surely there are other people in your life that you care about?“"
    show ym mnormal
    YM "“There aren’t, you’re the only one that matters.“"
    menu: 
        "(Oh? I kinda like that)":
                MC "(I get that this is all a little much by conventional standards but I’m kinda into it.)"
        "(Yikes, what is wrong with him?)":
                MC "(That is NOT the Nix that I know.)"

    show ym mhappy
    YM "“You’re the only person worth caring about...“"
    show ym mwhine
    YM "“So please, let me take care of you. You just seem really tired lately and all I want is for you to be happy.“"
    YM "“Please...let me be useful to you, [MC]..I can do so much for you...“"
    YM "“I can cook right? You like my cooking? Even if you don’t. I promise I’ll learn what you like!“"
    show ym mgrin
    YM "“Or if you just need eye candy, I’m always here for you. Dress me up in anything you like.“"
    YM "“Anything so that I can be yours.“"
    show ym mbtouched
    YM "“Please [MC], won’t you give me the honor of being by your side? Let me serve you.“"
    YM "“Please?“"
    menu: 
        "Y’know what? I’m down.":
                $ YM_dp = 0
                show ym mbctouched
                YM "“Is that a yes...?!“"
                MC "“Yes sweetie, It is.“"
                show ym mbsqueal
                "With that, I lean towards him and give him a little peck on his cheek. He jolts in surprise but soon lets out the most adorable little squeal."
                "He then moves from his current position to my lap and nuzzles right into the crook of my neck as he wraps his arms around me."
                show ym mworry
                YM "“So, you love me back right? I’m not just dreaming?“"
                MC "“No, you’re not."
                show ym mrbhappy
                "I give him a light squeeze in reassurance before gently patting his head."
                MC "“I love you too, Nix.“"
                show ym mapologetic
                YM "“Gosh, [MC], I can drop dead in your hands right this moment and I’ll still be happy...“"
                MC "“Please don’t, I can’t let a cute boy like you die in my lap.“"
                show ym mconcerned
                YM "“[MC], I’m really the only one for you right?“"
                MC "“Yes sweetie, you are.“"
                show ym mquestioning
                YM "“What about that guy downstairs?“"
                MC "“He’s just my neighbor.“"
                show ym mconcerned
                YM "“Still...“"
                MC "“You don’t need to be so jealous of him. After all, you’re the one who’s sleeping with me.“"
                show ym mapologetic
                YM "“Oh how long I’ve waited to hear you say that.“"
                show ym mcontent
                YM "“I’ve waited so long for you to reciprocate my feelings.“"
                YM "“To hold me in your arms like this.“"
                show ym mbtouched
                YM "“Ever since I’ve met you, all I’ve ever wanted to be is yours.“"
                MC "“And that’s what you’ll be from now on.“"

        "Okay stop that, give me some time.":
                $ YM_dp +=3
                show ym mconcerned
                YM "“[MC]?“"
                MC "“Give me some time okay? You can’t just spring all of this on me.“"
                show ym mwhine
                YM "“[MC], you don’t understand...!“"
                MC "“Nix, I care for you a lot but this is a bit much.“"
                show ym mwhinecry
                YM "“‘It’s him, isn’t it?!“"
                YM "“He’s the one you want ??!“"
                MC "“No, it’s not about-“"
                show ym mwhinecry:
                    linear 0.050 xoffset -10
                    linear 0.050 xoffset +0
                    linear 0.050 yoffset -10
                    linear 0.050 yoffset +0
                YM "“DON’T LIE TO ME!!“"
                show ym mhorrified
                YM "“I see the way he looks at you, the way he can’t take his eyes off of you , he likes you!“"
                MC "“You’re delusional.“"
                show ym mwhinecry
                YM "“I’M NOT! You just don’t see it!“"
                MC "“Even if that’s true, I don’t want to date him either.“"
                MC "“I didn’t tell you to give me some time because I ‘had someone else in mind’.“"
                show ym mmad
                YM "“Then.. what? What am I lacking? Why do I have to wait even longer to have you? To be yours?“"
                show ym mhorrified
                MC "“Let’s stop here. We should eat, your hard work is getting cold.“"
                MC "“As I said, give me some time.“"
                show ym mwhine
                YM "“fine...“"

    scene insiden with fade
    MC "(Today sure was wild.)"
    MC "(I think I tired myself enough. I mean Nix is already asleep by this this point.)"
    MC "(I’ll have to sleep too.)"
    MC "(Good night, Nix.)"
    
    scene highschooldream
    play music "audio/ed6.mp3" fadein 1.0 
    #yg buat mimpi bgm yg music box ini
    show ym hsangry
    GTWU "“stupid teachers, can’t believe they think I can finish all this before the school closes down“"
    GTWU "“i don’t get it“"
    GTWU "“i hate this...“"
    MC "“Is that for Mrs. Athens math class?“"
    show ym hsnormal with vpunch
    GTWU "(!!)"
    MC "“Sorry, did I scare you?“"
    GTWU "“no“"
    MC "“Man, that’s a lot of math questions. Why are you doing them here?“"
    GTWU "“Mrs. Athens said I couldn’t go back unless I finish them all“"
    MC "“Damn that sucks.“"
    show ym hsquestioning
    GTWU "“so why are you here?“"
    MC "“Group project, told my dad to pick me up at 5 but turns out we finished early.“"
    MC "“Now I have to wait.“"
    show ym hsnormal
    GTWU"“hm“"
    MC "“Actually, can I look at the questions? I’m bored.“"
    show ym hsquestioning
    GTWU "(what kinda sicko does math questions when they’re bored?)"
    GTWU "“sure?“"
    GTWU "(what [player_sb] [player_gender] doing?)"
    MC "“Wait a minute, I did these earlier!“"
    show ym hsnormal
    GTWU "“oh“"
    MC "“You wanna look at the answers? I already confirmed with Mrs Athens that they were right.“"
    show ym hsquestioning
    GTWU "“this isn’t a trick is it?“"
    MC "“No? I can teach you while we're at it, might as well review what I learned today.“"
    show ym hsangry
    GTWU "([player_gender] [player_sb] too close!!)"
    GTWU "“why are you talking to me?“"
    MC "“Because I’m bored? Besides, don’t you want some help with those? You’ll never finish at this rate.“"
    show ym hsnormal
    GTWU "“fine...“"
    
    scene hallwaydream with fade
    show ym hsnormal
    GTWU "(I didn’t expect this but [player_gender] really stayed and helped me finish all this)"
    MC "“And we’re done!“"
    MC "“Thanks for letting me help you, I would’ve been bored out of my mind otherwise.“"
    show ym hsquestioning
    GTWU "(and {i}I’m{/i} the one being thanked for this?)"
    show ym hsnormal
    GTWU "“no, thankyou for helping me“"
    GTWU "([player_possessive] scent, it’s nice...)"
    MC "“No problem! It doubles as me studying for next week's test anyway.“"
    MC "“Since our math questions are the same, I’m guessing we’re in the same grade?“"
    show ym hsquestioning
    GTWU "“maybe?“"
    MC "“I’m in class 2, you?“"
    show ym hsnormal
    GTWU "(oh? I know [player_possesive] class now)"
    GTWU "“3“"
    MC "“Guess that explains why I’ve never seen you around.“"
    MC "“Oh shit, It’s 5. I’m gonna head out first, bye!“"
    show ym hsquestioning
    GTWU "“bye? I guess“"
    show ym hsangry
    GTWU "(why did I say that? stupidstupidstupid)"
    GTWU "(why am I like this?)"
    GTWU "(and I don’t even know [player_possessive] name...)"
    show ym hsnormal
    GTWU "(I hope I meet [player_object] again)"
    jump ymlater

label month_tsm:
    #TSM End of Month"
    scene black with fade
    TSM "“Hey wake up.“"
    MC "(?)"
    TSM "“Wake up stupid, if ya don’t wake up now you’re gonna be late.“"
    TSM "“Geez, get an alarm or something.“"
    scene insidepd with fade
    MC "“Mornin’“"
    show tsm nnormal
    TSM "“Yea.“"
    show tsm nsilent:
        parallel:
            ease .5 zoom 1.3
        parallel:
            yalign 0.0
            linear 0.0 yalign 0.0 xalign 0.5
    "He gives me his hand and I grab it to steady myself, settling to our now familiar routine."
    "By this point, it’s almost the end of the month. In just a few days, we’ll be back to what we were like before."
    "And the worst part is I haven’t been able to make anYMore moves since we suddenly got busy due to finals."
    "One of us is always coming home late from either studying, finishing up group projects, or something else entirely."
    "Even Rudy has settled on cooking all our meals in the morning so whoever comes back first can just reheat them."
    MC "(I’ve been Rudy deficient, and by extension, maid boy deficient.)"
    MC "(Oh how I miss the sight of him in that dress and apron combo.)"
    MC "(Curse you finals week!!)"
    show tsm nuhsure
    TSM "“What’s with that look on your face?“"
    MC "“‘Oh come on, that’s just what I look like.“"
    show tsm normal
    TSM "“No, that’s what you look like when somethings bothering you.“"
    TSM "“So what is it? I can stay for another 15 minutes.“"
    TSM "“I’ll listen while you eat breakfast.“"
    show tsm nsilent
    MC "“You wanna hear the truth?“"
    show tsm nnormal
    TSM "“Yea.“"
    show tsm nsilent
    MC "“I miss seeing you in that maid outfit.“"
    show tsm nhuh
    TSM "(!!)"
    show tsm nnormal
    TSM "“Quit messin’ with me, you just woke up.“"
    show tsm nsilent
    MC "“I’m not messing with you. You never believe me when I say you look cute.“"
    show tsm nnormal
    TSM "“That’s cause I’m not.“"
    show tsm nsilent
    MC "“Keep lying why dont 'cha.“"
    show tsm nnormal
    TSM "“You’re weird.“"
    show tsm nuhsure
    TSM "“Genuinely though, what's up?“"
    show tsm nsilent
    MC "“I’m serious, I’m having a maid boy deficiency.“"
    MC "“My motivation is at an all time low right now and only you can help me.“"
    show tsm nhuh
    TSM "“Are you serious?“"
    MC "“When am I ever unserious?“"
    show tsm nnormal
    TSM "“All the time.“"
    MC "“Rude.“"
    show tsm nsmirk
    TSM "“Whatever.“"
    show tsm nsdnormal
    TSM "“Well, if you really wanted to...“"
    TSM "“I’m not too busy tonight.“"
    MC "“Oh?“"
    show tsm nangy
    TSM "“Don’t ‘oh?’ me, ugh {size=-10}why did I say that? {/size}“"
    show tsm ndeflecting
    TSM "“A-anyway, what time will you be back?“"
    show tsm nsilent
    MC "“Hopefully before 6, I don’t think I have anything else today.“"
    show tsm nhappy
    TSM "“Great, see you later. I’m gonna head out.“"
    MC "“See ya’.“"
    
    scene campus1d with fade
    MC "(Damn, I can’t believe the months almost over.)"
    MC "(And by extension, finals are approaching. This sucks.)"
    MC "(I used to be really studious, what the fuck happened to me?)"
    show ls normal:
         linear 0.050 xoffset -10
         linear 0.050 xoffset +0
    LS "“OH HEY! [MC], right?“"
    show ls normal at right
    show fs normal at left
    FS "“Don’t yell so loud, you’ll scare [player_object] off.“"
    MC "“Sorry. Do I know you two?“"
    FS "“Oh shit yea, you might not remember us.“"
    FS "“We’re Rudy’s friends.“"
    show ls normal:
         linear 0.050 xoffset -10
         linear 0.050 xoffset +0
    LS "“Yea! We’re part of the badminton club with him.“"
    LS "“You might’ve seen us sell cakes to fundraise for the club!“"
    MC "(Now that I think about it, I do remember something like that.)"
    MC "“I see.“"
    LS "“Now that we’re acquainted, can I ask you something?“"
    LS "“Upon hearing that, his friend immediately facepalms.“"
    FS "{size=-7}“You can’t just ask that. We gotta build up first.“{/size}"
    LS "“No use beating around the bush though. So [MC], what do you like in a guy?“"
    MC "“Huh“?"
    GTWU "{size=-15}“DON’T. WHY WOULD YOU ASK THAT.“{/size}"
    "I turn around to see the source of the noise but see no one."
    MC "“Did you guys hear that?“"
    FS "“Hear what? I didn’t hear or see anyone.“"
    show ls normal:
         linear 0.050 xoffset -10
         linear 0.050 xoffset +0
    LS "“Me neither!“"
    #bush noises
    "I turn around once more and finally spot Rudy, hiding in the bushes, looking as embarrassed as can be."
    MC "(I guess this is related to him, huh?)"
    show fs normal:
         linear 0.050 xoffset -10
         linear 0.050 xoffset +0
    FS "“Hey, don’t turn around! There’s no one there we swear!“"
    show ls normal:
         linear 0.050 xoffset -10
         linear 0.050 xoffset +0
    LS "“Yea, totally!“"
    MC "“Hmm.“"
    MC "(I guess I might as well play along.)"
    MC "{i}“Oh boy, I guess you’re right! I didn’t see a single person there!“{/i}"
    MC "“But still, the view on this side of the street is nicer to look at!“"
    FS "“So you don’t wanna turn around and face us?“"
    MC "“Sorry guys, the view is fantastic. Definitely {i}not{/i} because I saw someone hiding in the bushes.“"
    "After the words leave my mouth, Rudy peeks his head even further above the cover of the bushes, seeming vaguely pleased at himself."
    "I look back at his friends who grimaced in return and they soon rush to the other side of the street, where Rudy is. Perhaps hoping to cover my view of him."
    FS "“You’re sure you didn’t see anyone, right?“"
    MC "“Nope! Just you two.“"
    FS "“Good.“"
    LS "“Anyway, what kinda guy do you like? And no, this is NOT for Rudy.“"
    MC "(Which means it is for Rudy.)"
    "I glance at Rudy in the bushes, he stares at me expectantly, seemingly nervous at what I’m about to say."
    menu:
        "Men that can cook, It’d be great if they have a ponytail! Maybe their name starts with an ‘R’?":
                    "Rudy’s jaw falls wide open as his cheeks get redder, he stares wide eyed as if he can’t quite process what he just heard."
                    LS "“I see! So anyway we have this friend who’s really into you and they happen to be precisely your type!“"
                    MC "“Sounds great! Does his name end with a ‘Y’ perhaps?“"
                    LS "“It does!“"
                    MC "“Does he play badminton?“"
                    show ls normal:
                        linear 0.050 xoffset -10
                        linear 0.050 xoffset +0
                    LS "“WOW! How did you know?“"
                    MC "“I had a feeling.“"
                    FS "{size=-10} “Well, that’s good news for Rudy.“{/size}"
                    LS "“I know!“"
                    FS "“Thanks for your answer, It’ll help our friend a lot!“"
                    MC "“Sure thing.“"
                    hide ls
                    hide fs
                    show tsm nsilent
                    "When his friends eventually pass the bush, Rudy springs out of there, acting as nonchalantly as he could."
                    "He locks eyes with me and with a nudge from his friend, walks straight up to me."
                    show tsm nsdnormal:
                        parallel:
                            ease .5 zoom 1.3
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.0 xalign 0.5
                    TSM "“Uh, hi.“"
                    TSM "“I definitely just got here.“"
                    show tsm nsilent
                    MC "“Oh, I know that.“"
                    show tsm nuhsure
                    TSM "“So...umm. You’re not busy tonight right?“"
                    MC "“I’ll make time.“"
                    show tsm nhappy
                    TSM "“Cool.“"
                    show tsm nsdquestioning
                    TSM "“D-don’t come back too late okay?“"
                    TSM "“I...uh-“"
                    TSM "“I’ll be waiting.“"
                    MC "“Alright then, can’t wait.“"
        "Someone cute and sweet. Always there to help me out.":
                    $ YM_dp +=10
                    "Rudy looks in horror at my statement, seemingly crushed by every word in my sentence."
                    show fs normal:
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.0 xalign 0.4
                    FS "“Cute and sweet?“"
                    FS "“Yikes, he’s gonna need to work on that.“"
                    MC "(Okay, we’re definitely talking about Rudy. They’re not even hiding it anymore.)"
                    show ls normal:
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.0 xalign 0.6
                    LS "“Cute is subjective! I believe in him.“"
                    FS "“Well, to start with, he needs to stop calling people ‘stupid’ to hide his embarrassment.“"
                    LS "“Maybe that’s cute to some people?“"
                    MC "“So,  mind telling me what this is about?“"
                    FS "“Oh, it’s nothing! Just-“"
                    show ym nrhappy with vpunch:
                        parallel:
                            ease .5 zoom 1.5
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.0 xalign 0.25
                    show fs normal:
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.0 xalign 0.6
                    show ls normal:
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.0 xalign 0.8
                    YM "“Hey, [MC]!“"
                    "Nix runs and dives straight into my back, enveloping me in a tight back hug."
                    MC "“Whoa, what the fuck, Nix? You spooked me.“"
                    show ym napologetic
                    YM "“Sorry.. I just wanted to see you...“"
                    FS "{size=-10}“Yikes, Rudy has some stiff competition.“{/size}"
                    LS "“Rest in Peace my guy.“"
                    show ym nmtch
                    MC "“Again, mind telling me what this is about?“"
                    show ym ngrin
                    FS "“It’s nothing! We’ll take our leave now.“"
                    LS "“Uh YEA! Bye, [MC]!“"
                    MC "“See you two some other time?“"
                    MC "“Oh, and say hi to Rudy for me!“"
                    LS "“Will do!“"
                    hide ls
                    hide fs
                    #Hide sprite
                    show ym nnormal
                    YM "“[MC], who are those people? They were clearly hitting on you.“"
                    MC "“No they weren’t.“"
                    show ym nhuffy
                    YM "“You don’t know that! There’s absolutely no reason for anyone to not like you!“"
                    MC "“Everyone has their own thing. Anyway, can you please not hug me?“"
                    show ym napologetic
                    YM "“Sorry...I got excited when I saw you...“"
                    MC "“That’s fine, I’m just not a big fan of being hugged like that.“"
                    show ym nrhappy
                    YM "“Oh gotcha!“"
                    show ym nhappy
                    YM "“Anyway, you wanna walk together to class?“"
                    show ym nsmile
                    "I look at the bushes where Rudy was before only to see that he’s not there anymore. He already ran off, far into the distance with his friends."
                    MC "(Guess I’ll be walking with Nix.)"
                    MC "Sure, same as usual, yea?“"
                    show ym nhappy
                    YM "Yea.“"
                    show ym nmnormal
                    YM "{size=-10}{b}“Same as usual.“{/b}{/size}"
    
    if YM_dp == 10:
        scene roadevening with fade
        MC "(Ooh, I can’t wait to get back!)"
        MC "(Based on what he said this morning, I have a feeling Rudy has something planned tonight.)"
        MC "(I wonder what it is.)"
        scene kose with fade
        MC "(I’m back bitch!)"
        MC "(Can't wait to just-)"
        play sound "audio/punch.mp3"
        pause
        MC "(WHAT WAS THAT?!)"
        show tsm mdeflecting with moveinright
        TSM "“[MC]! Run!“"
        MC "“Holy shit! What’s going on?“"
        show ymed2mad at right with moveinright
        show tsm mangry at left with move   
        YM "{b}“Don’t go with him, [MC].“{/b}"
        show ym ed2angry at right with vpunch
        MC "“NIX??“"
        MC "(What’s going on? Why is he also in a maid outfit? And what’s with the knife?!)"
        show ym ed2angry:
            linear 0.050 yoffset -10
            linear 0.050 yoffset +10
        YM "“Don’t you dare come between me and [MC]! {b}I’m{/b} the one who’s supposed to be living with [player_object].“"
        show tsm mnormal    
        TSM "“Fuck you.“"
        play sound "audio/potbreak.mp3"
        show ym ed2hurt:
            linear 0.050 xoffset -10
            linear 0.050 xoffset +10
            linear 0.050 yoffset -10
            linear 0.050 yoffset +10
        YM "“OW!“"
        show ym med2angry    
        YM "“You. {b}You{/b} Don’t get in my way!“"
        show tsm mdeflecting    
        TSM "“What way asshole?! You broke into the room and swung a knife at me!“"
        show tsm msilent at right with move
        show ym ed2angry at left with move    
        YM "“[MC]’s mine!“"
        show tsm mangry    
        TSM "“Stay back!“"
        show ym ed2mad    
        YM "“It’s not {I}fair{/I}. I’ve known [MC] since highschool and you just swooped in and took [player_object] away from me!“"
        YM "“It’s not fair..It’s not fair, not fair, not fair, notfair, notfair, notfair, notfair, notfairnotfairnotfairnotfair!“"
        play sound "audio/punch.mp3"
        show tsm mstopit:
              linear 0.050 yoffset -10
              linear 0.050 yoffset +10
       
        YM "“S-shit!“"
        show ym ed2hurt:
                    linear 0.050 xoffset -10 
                    linear 0.050 xoffset +0 
                    linear 0.050 yoffset -10
                    linear 0.050 yoffset +0
        "Nix fell backwards landing on his back, his knife flung out of his arms right near me."
        show tsm mdeflecting 
        show ym mhorrified    
        TSM "[MC]!"
        menu:
            "Grab the knife.":
                    "On instinct, I head straight for the knife. Letting Rudy be the one to handle Nix while he’s down."
                    "Nix isn’t particularly strong but he was definitely scary when he had that knife."
                    "I can’t let my guard down around him."
                    play sound "audio/punch.mp3"
                    show ym mwhine:
                                linear 0.050 xoffset -10 
                                linear 0.050 xoffset +0 
                                linear 0.050 yoffset -10
                                linear 0.050 yoffset +0
                    YM "“AGH!“"
                    show tsm mangry    
                    TSM "“Don’t move asshole.“"
                    MC "“I got the knife!“"
                    TSM "“Good, now call the police!“"
            "Kick Nix while he’s down.":
                    show ym ed2hurt:
                        parallel:
                            ease .5 zoom 1.3
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.0 xalign 0.25
                    "The moment I saw Nix trying to get up, my feet moved straight to put him back on the ground."
                    play sound "audio/punch.mp3"
                    show ym mwhine:
                                linear 0.050 xoffset -10 
                                linear 0.050 xoffset +0 
                                linear 0.050 yoffset -10
                                linear 0.050 yoffset +0
                    YM "“Agh...! Ow...“"
                    show ym mhorrified    
                    show tsm msmirk:    
                          linear 0.050 yoffset -10
                          linear 0.050 yoffset +10
                    TSM "“DAMN! Fuck it up, [MC]!“"
                    show ym mwhinecry    
                    YM "“[MC]...you too...?“"
                    YM "“D-do I really...not have a c-chance?“"
                    MC "“Don’t even think about reaching for that knife.“"
                    YM "“Hngh...! w..why..?“"
                    TSM "“I’ll call the police!“"

        show ll normal with vpunch    
        LL "“What’s going on out here?!“"
        MC "(Oh shit, this looks really bad.)"
        show tsm mnormal    
        TSM "“He had a knife.“"
        show tsm msilent
        "With no hesitation, he points at Nix who is pinned on the ground, devastatingly close to sobbing his heart out."
        show tsm mnormal
        TSM "“Check the camera footage. You’ll see him breaking into one of the rooms while carrying a knife.“"
        TSM "“Also, we gotta call the police or something. I don’t feel safe with this guy around.“"
        
        scene kosn with fade
        "Surprisingly, the police came pretty quickly and after questioning us and reviewing the security footage Nix was carried off in the car, probably taken away for further questioning."
        "We decided to head straight back to the room, not wanting to deal with any more nonsense tonight."
        
        scene insidepd with fade
        play music "audio/romance.mp3" fadein 1.0
        show tsm msdangry    
        TSM "“Well shit, that was not how I expected the night to go.“"
        MC "“Me neither.“"
        show tsm msdnormal
        TSM "“And uh, sorry for getting the guy you like arrested...“"
        MC "“Huh? Where is this coming from?“"
        TSM "“I heard you like guys that are cute and sweet and always around, and I guess that guy fits the description.“"
        show tsm mnormal
        TSM "“Until he tried to kill me that is.“"
        MC "“Hey, I’m not into Nix.“"
        show tsm mhappy
        TSM "“Yea, I can see why now.“"
        MC "“No, even before that. I was into someone else.“"
        show tsm munsure
        TSM "“W-who?“"
        MC "“You silly.“"
        MC "“It was always you.“"
        show tsm msdnormal
        TSM "“You don’t have to lie y’know? I’m not hurt if you just tell the truth.“"
        MC "“I’m not lying.“"
        show tsm mstopit
        TSM "“D-don’t lie. Just like with this maid dress you made me wear, you were lying when you said I looked cute in it.“"
        MC "“I would NOT lie about that!“"
        MC "“You are fucking cute!“"
        show tsm mangry
        TSM "“D-don’t {i}lie{/i} and get my hopes up!“"
        MC "“I’m not!“"
        #mulai nangis"
        show tsm msdcquestioning
        TSM "“You are! You just wanna tease me and make me look even stupider than I already do in front of you.“"
        MC "(...)"
        TSM "“All those nice things you said when I first wore the outfit, they made me...happy.“"
        TSM "“B-but I know I’m not someone who fits that description...“"
        TSM "“Shit,  I just wanted to do a few nice things for you before I move out and this is what happens...“"
        show tsm msad
        "I look around the room and see what he was planning on doing before Nix attacked. Our usual picnic table was set up with a few unlit candles decorating it. "
        "He made extra side dishes and I see a small plate of cookies as dessert."
        MC "(And all this...is for me?)"
        MC "“Rudy, I don’t know who lied to you before. But I do think you’re cute, and you are very sweet.“"
        MC "“I mean, look at all this. You set this up for me.“"
        MC "“I don’t deserve this.“"
        show tsm msdcquestioning
        TSM "“You do though. I’m just paying you back. You befriended me back when college started even when I was kinda rude to you.“"
        TSM "“You weren’t mad at me when I led us to the wrong hall for the orientation.“"
        TSM "“You gave me that stomach medicine when I was keeled over in pain.“"
        TSM "“You even let me stay with you for free...“"
        show tsm msdcsure
        TSM "“You’re just...{i}nice{/i}“"
        TSM "“And I-I love you...“"
        MC "“Rudy...“"
        MC "“I love you too.“"
        show tsm msdcquestioning
        TSM "“N-no way.“"
        MC "(Oh come on.)"

        scene black with fade
        "Getting impatient, I grab his face and slam his lips into mine. He freezes up a little, seemingly unsure on what to do before settling on letting his hands roam somewhere around my back."
        "Feeling like he finally reciprocated my feelings, I don’t pull back and instead, I pull him even closer to me by his waist as he makes the cutest little whimpers."
        "Only when I’m out of breath do I finally stop."
        scene inside with fade
        show tsm msdcsure
        TSM "“[MC]...So you really do like me?“"
        TSM "“Y-you’re not just.. teasing me or anything, right?“"
        MC "“Of course not.“"
        show tsm mbsure
        TSM "“Shit, you make me so happy...“"
        MC "“You do too.“"
        show tsm mbsdquestioning
        TSM "“Actually, I got one extra surprise for you.“"
        MC "“There’s more?“"
        #cg sini!!! wajib"
        show ed2ver1 with fade    
        $ persistent.ed2ver1_unlocked = True
        TSM "“Here...“"
        TSM "“Thought it would make you happy.“"
        "He pulls up his long skirt, finally revealing his legs and the stockings that were hidden under there. It’s certainly prettier than I thought, and the garter just made him look extra hot."
        MC "“Holy shit, you’re incredible.“"
        TSM "“R-really?“"
        MC  "“You’re so pretty!“"
        show ed2ver2    
        $ persistent.ed2ver2_unlocked = True
        TSM "“Y-you think so? I bought these for today. You were always raving about ‘cute boys in maid outfits’, so...I figured I’d provide extra service.“"
        TSM "“So, how is it...?“"
        MC "“10 out 10 that’s for sure!“"
        MC "“You bought this even when you thought I didn’t like you back?“"
        TSM "“Well, you weren’t gonna see it anyway with the long skirt and all. I figured I’d take a chance here.“"
        MC "“It paid off, you look beautiful.“"
        MC "“All this, just for me?“"
        TSM "“Y-yea, just for you.“"
        MC "“Come here then pretty boy.“"
        scene black with fade
        "With that I climbed on top of him to give him another kiss, our bodies pressed together for warmth. Unbelievably soft sounds escaping his lips."
        "Living together with him might have been temporary at first, but starting now it might be something for the future as well."
        "Ending 2: Pretty Boy"
        
    else:
        scene roadevening with fade
        MC "(HE LIKES ME BACK!!!)"
        MC "(Or at least I’m pretty sure he does, judging from that awkwardly endearing interaction we had earlier at campus.)"
        MC "(I have a feeling he’s planning on doing something special though, maybe I should also get him something back?)"
        MC "(But what?)"
        GTWU "“Hey, Is that, [MC]?“"
        MC "“Huh?“"
        show ls normal at right
        show fs normal at left    
        "Turning around, I see his two friends for the second time today."
        MC "“Oh, hi! What’s up?“"
        FS "“We’re walking home.“"
        LS "“Shouldn’t you hurry up and see what Rudy has planned for you?“"
        MC "“That’s the thing, if he’s planning something for me then I should give him something back.“"
        MC "“Not sure what though, I feel like it’d be lazy if I bought him pudding again.“"
        FS "“Fair point.“"
        FS "“Damn, has he needed anything recently?“"
        LS "“Um, not really? We haven’t had to buy anything for our classes or class activities recently.“"
        LS "“Umm, let’s see...“"
        LS "“I don’t really know.“"
        MC "“Damn, thanks anyway.“"
        FS "“Sorry we can’t help.“"
        MC "“That’s fine. I’ll just look around the stores for something.“"
        LS "“Alright, bye future friend-in-law!“"
        FS "“Bye, [MC].“"
        MC "“Yea, byee.“"
        hide ls
        hide fs    
        MC "(What the fuck do I buy him on such short notice?)"
        MC "(Wait I got it!)"
        MC "(I can make a little kit for him with things he might need. After all, I think I’ve gotten to know him better by living him.)"
        scene supermarket with fade
        MC "(Let’s see, first we need a pouch of sorts to hold everything. Hopefully nothing too big.)"
        MC "(Ah, this should do.)"
        jump medicines

label medicines:

    $ Bandages = False
    $ Stomach = False
    $ Sunscreen = False
    $ Salonpas = False
    $ Sanitizer = False
    $ WetWipes = False
    $ HandCream = False
    $ FeverPatch = False
    $ Thats = False

label choose_medicines:

    if Bandages and Stomach and Sunscreen and Sanitizer and Salonpas and Sanitizer and WetWipes and HandCream and FeverPatch and Thats:
        jump TSMafterloop2

    menu:
        MC "“Then I can fill it up with a small packet of tissues, maybe a notepad and...“"

        "A few bandages" if not Bandages:
            $ Bandages = True
            jump choose_medicines

        "Stomach Medicine" if not Stomach:
            $ Stomach = True
            jump choose_medicines

        "Small bottle of Sunscreen" if not Sunscreen:
            $ Sunscreen = True
            jump choose_medicines

        "Salonpas" if not Salonpas:
            $ Salonpas = True
            jump choose_medicines

        "Hand Sanitizer" if not Sanitizer:
            $ Sanitizer = True
            jump choose_medicines

        "Wet Wipes" if not WetWipes:
            $ WetWipes = True
            jump choose_medicines

        "Hand Cream" if not HandCream:
            $ HandCream = True
            jump choose_medicines

        "Fever Patch" if not FeverPatch:
            $ FeverPatch = True
            jump choose_medicines

        "That's All" if not Thats:
            $ Thats = True
            jump TSMafterloop2 

label TSMafterloop2:
            MC "(Alright, I hope that’s enough. After all, Rudy’s waiting for me back at our place.)"
            "Quickly, I ran to the cashier with all of my chosen items. Once I’ve placed everything on the conveyor belt, I prepare my phone to pay."
            MC "“Oh, can you please put everything in the pouch? I don’t need a shopping bag either"
            C "“Okay.“"
            C "“Oh wait! You’re the cute couple, how’s he doing?“"
            MC "“Great, I’m buying all this to make a little emergency kit for him.“"
            C "“Aww, you two sure are cute.“"
            C "“Anyway this is your total, paying with the QR code again?“"
            MC "“Yep.“"
            MC "Here you go.“"
            C "Thanks for shopping here.“"
            MC "“‘Sure thing.“"
            
            scene roade with fade
            MC "(Now, time to rush back.)"
            scene kose with fade
            MC "(I’m here.)"
            scene insidecandlelit with fade
            MC "Rudy, I’m back.“"
            MC "“Rudy?“"
            #cg sini"
            play music "audio/romance.mp3" fadein 1.0
            show ed3ver2 with fade
            $ persistent.ed3ver2_unlocked = True
            TSM "“Finally you’re back. Welcome home, [MC].“"
            "My eyes are immediately glued to Rudy. He’s sitting down on our picnic blanket with a few small candles around and his arms tied into a bow."
            "How he achieved that, is something that I’m not about to question."
            show ed3ver1
            $ persistent.ed3ver1_unlocked = True
            TSM "“You know how this morning you said you wanted to see me in a maid outfit again?“"
            TSM "“W-well, here I am.“"
            scene ed3ver2
            TSM "“All in a little bow, just for you.“"
            MC "“Holy shit... Rudy...“"
            "I quickly put away my belongings and headed straight on top of him. He doesn’t try to pull away, instead eagerly squirming under me."
            MC "“Is this all for me?“"
            TSM "“‘Yea, all for you, [MC].“"
            TSM "“B-because, I love you a-and I-“"
            scene ed3ver2
            TSM "“S-shit, I’m crying.“"
            MC "“It’s okay, shh. Take your time, I won’t leave.“"
            TSM "“O-okay, umm...“"
            TSM "“Well I’ve always wanted to keep it hidden. After all, we’ll be moving in a bit for our third semester and we might never see each other again.“"
            TSM "“But...I heard what you said earlier at campus.“"
            MC "(Oh, when he was hiding in the bushes?)"
            MC "“So you heard that?“"
            scene ed3ver2
            TSM "“Y-yea. And it suddenly clicked that maybe..you teasing me wasn’t a cruel form of punishment but instead...because you liked me?“"
            TSM "“Like, maybe you actually thought I was cute and stuff. You weren’t just lying to my face.“"
            MC "“I wouldn’t lie about that.“"
            scene ed3ver1
            TSM "“I know that now but...I had a hard time believing it this past month.“"
            TSM "“And it was torture, the [player_ds] I liked is right there in front of me and I had to continuously convince myself to not get my hopes up.“"
            TSM "“Especially when I’d see you at campus with your other friend. I couldn’t help but think that he was into you too or something.“"
            TSM "“I-I know that’s kind of a shitty thing to think about someone, but I w-was jealous.“"
            TSM "“Especially when I heard that you usually walk around with him.“"
            scene ed3ver2
            TSM "“So umm, despite all my shitiness, do you still want me? Are you really okay with someone like me?“"
            MC "“Rudy, there’s no one else I’d rather be with.“"
            scene black with fade
            "I use my dominant hand to tilt his chin upwards to me before placing a gentle kiss on his lips. I can feel him grow a bit more sure as he presses us together, the only thing between us being his tied up arms."
            scene ed3ver2 with fade
            "When I pull away, the smell of his home cooked meal wafts to my face, making me grow hungrier by the second."
            "Whether the hunger is for him or his cooking, I cannot tell."
            MC "“Shit...I love this so much.“"
            TSM "“Y-you do?“"
            MC "“Of course I do.“"
            MC "“Is you being tied up part of the surprise as well?“"
            TSM "“Y-yea. Go ahead, unwrap your present. I’m all yours.“"
            MC "“Thankyou for letting me do this, I love you.“"
            "Gently, I unwrap all the bow, layer by layer, freeing his arms from its temporary shackle."
            "He gestures at my thigh, as if asking for permission to place his hand there. I nod and he shakily caresses my thigh."
            MC "(He’s too cute.)"
            scene black with fade
            "Finally, I pull him back into another kiss, wrapping my arms around his shoulder."
            "He responds in kind, moving his arms around my back, holding me like a dream that might disappear any minute."
            "Luckily for him, I won’t. I’ll be here as long as he still loves me. And I’ll reassure him of my love whenever he needs it."
            "Ending 3: Candlelit Dinner"

label ymlater:
    #YM Later"
    if YM_dp >= 1:
        scene black with fade
        MC "(Was that...Nix? Back in highschool?)"
        MC "(Shit, not only is he living rent free at my place, he’s also living rent free in my head as well.)"
        play sound "audio/fabric.mp3"
        MC "(?)"
        play sound "audio/slap.mp3"
        scene insiden with fade
        MC "(What’s going on? It’s not a ghost is it?)"
        "A little spooked by the noise, I decided to squint my eyes open and check out the source of the noise."
        MC "(Is that...Nix?)"
        MC "(What is he up to this late at night?)"
        "In the darkness, I managed to make out his silhouette slowly walking towards the door. His hands are carrying something, but I can’t quite make out what."
        "Eventually, he quietly opens the door and disappears from my sight."
        MC "(Damn, what the fuck is he doing this late at night?)"
        MC "(Goddamit Nix. You can’t even let me sleep, huh?)"
        "Groggily, I get up from my bed, staggering in the darkness in my quest to figure out what he’s up to so late."
        MC "(Guess I gotta follow him.)"
        
        if YM_dp >= 5:
            play sound "audio/banging.mp3"
            MC "(OKAY, THAT’S NOT GOOD!!)"
            scene hallwayn with fade
            MC "(What happened?)"
            play sound "audio/banging.mp3"
            show ym smad
            "As soon as I ran downstairs, I saw Nix with a baseball bat, swinging it like a madman at Rudy’s door. It’s not doing much to the door but it is making a fuck ton of noise."
            play sound "audio/banging.mp3"
            MC "(Is he trying to break it down?!)"
            show ym sdesperate
            MC "“Nix what the fuck?!“"
            YM "“[MC]?!“"
            show ym scpleading
            YM "“N-no I swear, It’s not what it looks like!“"
            MC "“You’re swinging a baseball bat at someone’s door in the middle of the night!“"
            MC "“What is wrong with you?!“"
            show ym swhine
            YM "“Y-you don’t understand! He’s in my way!  I need to get rid of him so we can be together.“"
            MC "“No stupid, you need to stop this right now!“"
            show ym swhine at left
            show tsm suhsure at right
            TSM "“What the fuck is going on?!“"
            MC "“Rudy! Watch out!“"
            "Nix swings the baseball bat right at Rudy’s head, knocking him straight to the ground."
            show ym scwhine
            YM "{b}“Stay back!“{/b}"
            show ym smad at center
            TSM "“Agh..shit!“"
            MC "“Rudy!“"
            hide TSM
            "Seeing him on the ground like that made my heartbeat speed up like never before. It really dawned on me that Nix, the boy I’ve considered a good friend ‘till now, might be a threat to my life."
            show ym smad:
                    linear 0.050 xoffset -10 
                    linear 0.050 xoffset +0 
                    linear 0.050 yoffset -10
                    linear 0.050 yoffset +0
            "Acting on snap decisions, I ran up to him and kicked the bat out of his hands. He falls back, now weaponless if only momentarily."
            show ym scmdesperate
            YM "“[MC]?! What are you doing...? Please don’t stop me here. I {i}need{/i} to do this...!“"
            "I don’t listen, I immediately run over to grab the bat."
            show ym smcwhine
            YM "“PLEASE..!It’s for US! [MC]...“"
            "From the corner of my eye, I see Rudy wobbling back up before falling to his knees again."
            MC "“Rudy, run while you can!“"
            show ym scmdesperate
            YM "“Don’t root for him [MC]! You’re mine!“"
            "Nix lunges at me, trying to gain some control of the situation. Now armed with the bat, I give him a taste of his own doing with a sharp whack."
            play sound "audio/banging.mp3"
            show ll at right
            show ym smad
            LL "“What’s going on here?!“"
            MC "“Call the police! Or at least an ambulance! Just check the security footage later!“"
            LL "“Uhh....okay!“"
            hide ll
            show ym scpleading at center:
                    linear 0.050 yoffset -10
                    linear 0.050 yoffset +10
            YM "“[MC]..please...!!“"
            "He’s bleeding but his determination knows no bounds. He’s desperate enough that he rises back once more, trying to get the bat back."
            show ym swhine
            YM "“PLEASE, PLEASE...JUST LOVE ME AND I’LL STOP!!!“"
            YM "“I just need to be yours...!!“"
            MC "“No.“"
            "I tackle him to the ground, putting my weight on him so he won’t be able to get up."
            #kalau sempet cg"
            show ed4ver2 with vpunch
            $ persistent.ed4ver2_unlocked = True
            YM "“[MC]?“"
            YM "“Please...[MC]... Am I that unlovable to you...?“"
            YM "“C-can you really not love me...?“"
            scene ed4ver2 with vpunch
            play sound "audio/slap.mp3"
            MC "{b}“Don’t move.“{/b}"
            YM "{size=-10)“Ahh...shit.“(/size}"
            show ed4ver1 with vpunch
            $ persistent.ed4ver1_unlocked = True
            YM "“ahahaha...HAHAHAHA“"
            MC "(?)"
            YM "“AHAhaha..ha.ha..“"
            "Delirious and losing blood, Nix gives me a gleeful smile."
            YM "“W-well at least...if this is how it ends...“"
            YM "{size=-10}“I-it’s...by your hands...“{/size}"
            scene hallwayn with fade
            "Once the words leave his mouth, his eyes close as if he just said his final breath."
            "I place a hand to his chest, still sensing a heartbeat out of him."
            LL "“The ambulance is here!“"
            MC "“Get both of them to the hospital, now!“"
            MC "(This night certainly isn’t how I expected my college life to go, definitely a lot more dramatic than even my dreams.)"
            MC "(But at least, just for tonight. I survived.)"
            MC "(I don’t know how I’ll deal with the aftermath.)"
            MC "(But I’ll leave that as a problem for future me.)"
            "Ending 4 : Survived the Night"
        
        else:
            MC "(I sure hope he isn’t doing anything weird, he was pretty on edge earlier.)"
            scene hallwayn with fade
            "When I finally emerge downstairs, I see Nix squatting in front of Rudy’s door, wearing earphones with his phone in hand."
            MC "“Nix, what are you doing?“"
            MC "(He can’t hear me.)"
            "Lacking any sense of danger, I approached closer and leaned down behind him to see what he’s watching."
            MC "(It’s a tutorial on picking locks?)"
            MC "“Nix, what the fuck?“"
            show ym sdesperate
            YM "(!!!)"
            show ym sworry
            YM "“[MC]...?“"
            show ym scwhine
            YM "“N-no, you weren’t supposed to see this.“"
            MC "“What are you doing here?“"
            show ym sdesperate
            YM "“Nothing...!“"
            MC "“Are you trying to break into the room?“"
            show ym scwhine
            YM "“N-no! I would never.“"
            "I look over at his other hand where I see a bobby pin that is crudely fashioned into a lock picking tool."
            MC "“You’re not getting out of this.“"
            MC "“You’re fucking stupid, y’know that?“"
            show ym scpleading
            YM "“Hngh...![MC]...please...“"
            MC "“No, go back to my room.“"
            show ym scwhine
            YM "“B-but...!“"
            YM "“P-please...I just wanted to be a good boy for you...H-he was in the way...!“"
            MC "“Well you’re not being very ‘good’ right now, in fact I’d say you've been bad.“"
            YM "(!!)"
            MC "“{b}Go back. {/b} We’ll talk later unless you want me to hate you prolifically?“"
            show ym spleading
            YM "“No..! I’ll be good.“"
            MC "“That’s what I thought, now hurry up.“"
            
            scene inside night with fade
            MC "“So. mind explaining what you were trying to do?“"
            show ym sworry:
                        parallel:
                            ease .5 zoom 1.5
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.0 xalign 0.0
            YM "“W-well, It’s really not what you think-“"
            MC "{b}“Don’t lie.“{/b}"
            show ym scwhine
            YM "“Eek!“"
            show ym scpleading
            YM "“I’m sorry, okay?I really am.“"
            YM "“You were right, I was trying to get rid of him.“"
            show ym schurt
            MC "“How did you even know that was his room?“"
            show ym scpleading
            YM "“Um I..I-“"
            MC "“What?“"
            show ym scwhine
            YM "“I saw it by checking the security cameras in your place.“"
            show ym schurt
            MC "“You got access to where it is?“"
            MC "(Even I don’t know how to, It’s almost impressive if he wasn’t using the knowledge to do shit like this.)"
            show ym scworry
            YM "“Uh yea. It’s on the web. Anyone can access it.“"
            MC "“WHAT.“"
            show ym scwhine
            YM "“I’m sorry i’m sorry i’m sorry imsorry imsorry!!“"
            YM "“There’s this website that uploads footage from unprotected security cameras.“"
            YM "“If the camera’s password isn’t changed from the default, then It’ll show up there.“"
            YM "“Y-you can take it down if you ask!“"
            YM "“But most people don’t know it...“"
            show ym schurt
            MC "“So you’re telling me, that the activity inside the halls of this place can be viewed by random strangers on the internet??"
            show ym sworry
            YM "“Just the halls and the outside! Your room is safe.“"
            show ym sapologetic
            YM "“As much as I wanted to, I can't watch you 24/7.“"
            MC "“And {i}that{/i} is supposed to make me feel better?“"
            show ym sworry
            YM "“W-well...“"
            MC "“Is this why our schedule tends to line up so well?“"
            MC "“Because you’ve been watching me?“"
            show ym schurt
            YM "(!!)"
            MC "“Spot on aren’t I?"
            show ym scpleading
            YM "“I-I’m sorry...“"
            show ym schurt
            MC "“You should be.“"
            MC "“Anything else I should know about?“"
            show ym sworry
            YM "“No-! T-that’s really it...“"
            "Whatever character he usually puts on is long gone, those cheerful smiles and infinite pep in his step."
            "The boy in front of me is a little more broken than that, shaking from either the cold or the fear of being hated even more."
            MC "“I don’t believe you.“"
            play sound "audio/slap.mp3"
            #sprite nangis"
            show ym stear:
                    linear 0.050 xoffset -10
                    linear 0.050 xoffset +0
                    linear 0.050 yoffset -10
                    linear 0.050 yoffset +0

            YM "“Okay okay okay, I’ll tell you...!“"
            YM "“W-when you’re not around...I-I grab one of your shirts from the dirty laundry pile and sniff them b-because I miss you...“"
            play sound "audio/slap.mp3"
            show ym scwhine:
                    linear 0.050 xoffset -10
                    linear 0.050 xoffset +0
                    linear 0.050 yoffset -10
                    linear 0.050 yoffset +0                        

            YM "“Hngh..!“"
            MC "“Keep going.“"
            YM "“W-hen you’re asleep, I-I lay next to you and I-I kiss you...“"
            YM "“I-I didn’t bite you or anything...! I swear I didn’t do anything else! I-I didn’t wanna wake you up...“"
            play sound "audio/slap.mp3"
            show ym stear:
                    linear 0.050 xoffset -10
                    linear 0.050 xoffset +0
                    linear 0.050 yoffset -10
                    linear 0.050 yoffset +0

            YM "“Ow..! [MC]...why? I’m telling you everything...“"
            MC "“So, you don’t think your actions have consequences?“"
            MC "“Shouldn’t you be grateful that I’m even hearing you out?“"
            YM "“R-right...sorry, [MC]...“"
            show ym scpleading
            YM "“Sometimes, I-I go through your phone a-and go through your searches so I can be what you like...“"
            YM "“Umm well, y-you had an album full of maid outfits, s-so I assumed...“"
            play sound "audio/slap.mp3"
            show ym schurt:
                    linear 0.050 xoffset -10
                    linear 0.050 xoffset +0
                    linear 0.050 yoffset -10
                    linear 0.050 yoffset +0

            MC "“Bold, aren’t you?“"
            YM "“Hngh...!“"
            MC "“What else?“"
            show ym scworry
            YM "“I...I lied about being scared of the fire so you’d let me stay with you...“"
            MC "“Don’t tell me you caused the fire too?“"
            YM "“W-well-“"
            show ym schurts:
                    linear 0.050 xoffset -10
                    linear 0.050 xoffset +0
                    linear 0.050 yoffset -10
                    linear 0.050 yoffset +0

            play sound "audio/slap.mp3"
            show ym sdesperate
            YM "“Not directly! I swear!“"
            YM "“I just...convince a housemate to throw a candlelit dinner in his room for his girlfriend.“"
            MC "{b}“And?“{/b}"
            YM "“W-well, he had a hundred candles in there. Including near the door.“"
            YM "“I-I don’t know the specifics but-“"
            show ym scworry
            YM "“Some probably got knocked down whenever anyone opened the door.“"
            MC "“And so the fire started?“"
            YM "“M-maybe?“"
            show ym stear
            play sound "audio/slap.mp3"
            show ym sdesperate:
                    linear 0.050 xoffset -10
                    linear 0.050 xoffset +0
                    linear 0.050 yoffset -10
                    linear 0.050 yoffset +0
            YM "“[MC]...please...!! That’s all really...That’s really the end of it...“"
            show ym stear:
                    linear 0.050 xoffset -10
                    linear 0.050 xoffset +0
                    linear 0.050 yoffset -10
                    linear 0.050 yoffset +0
            play sound "audio/slap.mp3"
            show ym scwhine
            YM "“Really-! Everything else I just fantasize about doing...!“"
            YM "“I-I m sorry...! I really am! I’m sorry..I’m sorry I’m sorry“"
            "By this point, his tears have evolved to loud sobs, the teardrops falling down like a waterfall. His hands placed on his mouth in an attempt to silence himself."
            MC "“Is that all?“"
            show ym s
            show ym spleading
            YM "“Y-yes. I swear...“"
            MC "“Alright then, good boy.“"
            "Satisfied with what I pulled out of him, I relent and I sat down to his level and gave him a nice big hug."
            "Confused by my actions, he lets himself go limp in my arms like a doll. His head unmoving from the crook of my neck as I feel the wetness on my shoulders."
            "We stayed like that for a while, in the dark, with only his cries filling the room."
            "I pull him up to face me and I cup his cheeks which feel unnaturally cold."
            MC "“Does it hurt? From when I slapped you?“"
            show ym schurt
            "Words fail him, as he struggles to get his mouth to make any noise that isn’t a cry or a whimper. Eventually he settles for a frantic nod."
            MC "“I’m sorry sweetie, but you have to learn your lesson.“"
            MC "“Now listen closely, if you listen to me, you might get what you want.“"
            YM "!"
            show ym scbsurprised
            "His eyes lit up at my words and he gave me another frantic nod."
            MC "“We can date but I have a few rules for you.“"
            MC "“Number one being that you can’t infringe on my privacy like this, that means no going through my phone and no looking at me through security cameras.“"
            MC "“Can you understand that?“"
            show ym sapologetic
            YM "“Y-yes, [MC].“"
            MC "“Number two, you can’t attack or harass people just because you think they’re interested in me.“"
            show ym sworry
            YM "“O-okay...“"
            show ym sworry
            MC "“Last but not least. You have to communicate with me. Don’t lie to me.“"
            MC "“You got that? No hiding things from me.“"
            show ym sapologetic
            YM "“Yes, [MC]“."
            MC "“Good boy.“"
            "I give him a little peck on his forehead while my hands reach for his own. Holding his hands in mine, I give them a tight squeeze, something to assure him that I still care about him.“"
            
            show ed5ver2 with fade
            $ persistent.ed5ver2_unlocked = True
            YM "“D-does this mean that...you l-love me?“"
            MC "“Yes sweetie, as long as you follow my rules.“"
            MC "“You can do that for me, can’t you?“"
            show ed5ver1
            $ persistent.ed5ver1_unlocked = True
            YM "“Yes, yes, yes! I’ll be the best boyfriend you’ll ever have!“"
            YM "“I’ll be good from now on.“"
            MC "“That’s all I need you to be.“"
            scene black with fade
            "Finally, I seal the deal with a kiss to his lips. He hungrily accepts like a death row inmate who’s been starved for some time."
            "And it feels {I}right{/I}."
            "I can’t say for sure that I made the most rational decision tonight, but I know that it’s one I wouldn’t forget for the rest of my life..."
            "Ending 5  : Good Boy."
    
    else:
        scene black with fade
        MC "(Was that...Nix back in highschool?)"
        MC "(I guess we did meet back then...)"
        MC "(He sure changed a lot.)"
        scene insiden with fade
        show ym sapologetic
        YM "(!)"
        "When I opened my eyes, I’m met at the sight of Nix staring right back at me."
        show ym sworry
        YM "{size=-10}“[MC]...? You’re awake.“{/size}"
        MC "“Yea. What's up?“"
        YM "“I-I couldn’t sleep.“"
        MC "“Poor thing, come over here.“"
        show ym ssmile:
                        parallel:
                            ease .5 zoom 1.5
                        parallel:
                            yalign 0.0
                            linear 0.0 yalign 0.0 xalign 0.0

        "We were already laying side by side before but now we were wrapped in a tight embrace, sharing warmth under the blanket."
        MC "“Is this better?“"
        YM "“Hmm.“"
        show ym sapologetic
        YM "“Nothing could be better, [MC]...I don’t need anything else when you’re holding me like this.“"
        MC "“So why couldn’t you sleep earlier? Anything wrong?“"
        show ym scworry
        YM "“No...I just couldn’t stop thinking about you.“"
        YM "“Why are you still awake, [MC]? I wasn’t bothering you, was I?“"
        show ym schurt
        MC "“Relax sweetie, I had a good dream.“"
        MC "“I think it was of you.“"
        show ym shappy
        YM "“R-really...?“"
        MC "“Did you happen to wear a mask during highschool?“"
        YM "“N-no way, you remember me?“"
        show ym scwhine
        YM "“P-please forget about it...! I was so embarrassing...“"
        "He buries his face further into my chest in an attempt to hide his expression, I chuckle lightly and start to softly comb through his hair with my fingers."
        MC "“No you weren’t, you were very cute.“"
        show ym sworry
        YM "“Was I...?“"
        "He pulls away slightly, enough that I can see his face again."
        
        show ed6ver1 with fade
        $ persistent.ed6ver1_unlocked = True
        YM "“B-but I was so lame...I had no friends, I wasn’t smart, I wasn’t good at anything either...“"
        MC "“Doesn’t change the fact that you were cute.“"
        YM "“I did a lot of pathetic things back then...“"
        MC "“Like what? Tell me all about me.“"
        YM "“W-when your class was out for P.E, I’d sneak in and take a picture of your notes to study with.“"
        MC "“Did you? I’m sorry if you couldn’t read my handwriting...“"
        YM "“No, I’m sorry for doing it without permission...“"
        MC "“Did my notes help in any way?“"
        YM "“Of course they did! I-I couldn’t stop staring at them and reading them over and over and over again.“"
        YM "It g-got my grades up...“"
        MC "“Aww, I’m happy to hear that.“"
        YM "“I tried following you back to your house a few times...“"
        MC "“Really...?“"
        MC "“But I was on a motorcycle...and my house was quite far, you managed to keep up?“"
        YM "“I-I did! F-following you with my bike helped build my stamina...“"
        MC "“Did you go in?“"
        YM "“N-no...! I didn’t go that far..! I wouldn’t want to upset you...“"
        MC "“It’s okay, I can just invite you to visit during summer break.“"
        MC "“I’m proud that you tried to get your life together in college.“"
        show ed6ver2 
        $ persistent.ed6ver2_unlocked = True
        YM "“It was all for you, [MC]. All for you.“"
        YM "“I didn’t want you to be embarrassed by me...so I wanted to become someone more worthy of you.“"
        YM "“H-have I succeeded, [MC]?“"
        MC "“You have sweetie.“"
        scene black with fade
        "With that, I pull him into a kiss. His lips parted, giving me access to explore his mouth."
        "He just melted further and further with every little touch, making soft whimpers here and there."
        "He’s all I’ve ever wanted, and he’s all I’ve ever needed."
        "Hopelessly vying for every scrap of my attention, he’s offor every scrap of my attention, he’s officially {b}mine.{/b}"
        "Ending 6 : Mine"

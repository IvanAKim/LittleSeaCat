# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define Artin = Character("Artin")
define MrsWoodman = Character("Mrs.Woodman")
define Gordon = Character("Gordon")
define Oz = Character("Oz")
define MrWoodman = Character("Mr.Woodman")
define Daniel = Character("Daniel")
define Max = Character("Max")
define Leona = Character("Leona")
define Stephy = Character("Stephy")
define Stranger = Character("???")
define Claudine = Character("Claudine")
define Bill = Character("Bill")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    # e "You've created a new Ren'Py game."
    #
    # e "Once you add a story, pictures, and music, you can release it to the world!"
    # Background Black Screen

    Stranger "…"
    Stranger "It's dark."
    Stranger "…"
    Stranger "Where am I?"
    Stranger "What happened?"
    Stranger "… is that water I hear? …"
    Stranger "It sounds like … waves."
    Stranger "… how nostalgic."
    Stranger "I feel like I'm forgetting something."
    Stranger "What was it?"
    Stranger "A … a promise, I think."
    Stranger "… I made … a promise …"
    Stranger "…"
    Stranger "…"
    Stranger "…"

    # Background White Screen

    Stranger "Hey Daniel! It's time to wake up!"

    # Background Ship Cabin
    # Foreground Daniel, Stephy, Artin, Leona

    Stephy "Wake up, sleepyhead! We're almost at the island!"
    Daniel "W-what? What's going on?"
    Artin "You fell asleep reading your mystery novel."
    Leona "You looked so peaceful, we didn't want to wake you up."
    Daniel "Oh...right. We're on the ship."
    Stephy "Pretty soon, we'll have our VACATION!"
    Stephy "Come on! Let's head to the deck! You can see the island already!"
    Artin "Stephhy, calm down. Daniel just woke up, don't start dragging him around."
    Leona "Are we heading up together? Should we put away the playing cards?"
    Artin "Nah, just leave them there. It'll be my 26th consecutive win when we come back down-"
    Artin "HEY! Don't sneak a look at the next card on the deck!"
    Leona "Awww…"

    # Background Ship Deck

    Stephy "There it is! There it is!"
    Leona "It's pretty huge…"
    Leona "Artin, I still can't believe your family owns that entire island."
    Daniel "Thanks for letting us come along on your family trip, Artin. You're sure your parents are okay with us being here?"
    Artin "Yeah, we visit the island pretty often. My parents bring guests all the time- their friends, their coworkers, even random people they meet. You guys are totally fine."
    Artin "And in any case, we've finally graduated. We'll be going to college pretty soon- we should kick back and relax while we can."
    Leona "It's kind of sad to know that we'll be going our separate ways after this…"
    Stephy "…"
    Stephy "All the more reason to have as much fun as we can on this trip!"
    Daniel "Yeah!"
    Daniel "…"
    Daniel "…Um, you've been watching us for a while now. Do you need something?"

    # Foreground Claudine enters.

    Stranger "…Be careful by the railing."
    Daniel "…Oh."
    Daniel "Right. We will."

    # Foreground Claudine leaves.

    Stephy "Who's that lady?"
    Artin "I don't know, but she's probably another guest."
    Leona "…"
    Leona "Uh, the boat just got a lot faster."
    Leona "Who's driving this ship, anyway?"
    Artin "…my father."

    # Background Ship Bridge
    # Foreground Mr. Woodman, Mrs. Woodman, Max

    MrWoodman "HOOHAHAHAHAHAHA!"
    MrWoodman "Max, come on over! You can see the island up ahead!"
    MrWoodman "We're nearly there, let's step on the gas a little! Hahahahaha!"
    Max "…p-please s-slow down, M-Mr. Woodman…"
    MrWoodman "I can't hear you too well back there, sonny! Come out from under the table and speak up!"
    MrsWoodman "Arthur, maybe you should slow the boat down a little. You're going to make our passengers seasick."

    # Background Ship Deck
    # Foreground Daniel, Stephy, Artin, Leona

    Daniel "…Does your father happen to be an F1 racer, by any chance?"
    Artin "…hahaha…"
    Stephy "Wooooooohoooooooooo!"
    Leona "I'm glad I skipped lunch…"

    # Background Island Dock

    Stephy "We're hereeee!"
    Daniel "M-my l-l-legs…"
    Leona "H-how are y-you able to j-jump around l-like that?!"
    Artin "…sorry, Father usually drives too fast…"
    Stranger "Heeey!"

    # Foreground Bill enters

    Bill "I'm Bill, one of Mr. Woodman's business partners. He and Molly wanted me to tell you folks to head on over to the inn without them."
    Bill "They'll be coming shortly, right after they wrap up their conversation with Ms. Claudine."
    Bill "Which one of you is Artin? Arthur said you'd be able to lead the way."
    Artin "That'd be me. We can start walking as soon as everyone recovers."
    Bill "Ah, sea legs?"
    Bill "I understand. Pretty hard not to end up with a pair after that boat trip, hahaha!"
    Bill "…Although I see one of you is somehow still able to bounce around."
    Stephy "Come on, you guys!"
    Leona "If you've got so much energy, why don't you carry me over there!"

    # Background Pathway Along the Beach
    # Background Inn Front
    # Background Inn Reception

    Gordon "Artin! You're here! How was the trip?"
    Artin "Hey, Gordon. Father drove too fast again, but otherwise it was okay."
    Artin "Can we get keycards for these four?"
    Daniel "You don't need one, Artin?"
    Artin "My parents and I have our own rooms here. Don't worry, I already have my key."
    Gordon "…"
    Gordon "Artin…with friends. I thought I'd never see the day!"
    Artin "Gordon!"
    Gordon "Hahaha, I'm just joking!"

    # Background fade to Black Screen, then Inn Reception

    Gordon "…and here are your keycards."
    Gordon "You should be all set now, just take the stairs and head down the hallway to find your rooms."
    Gordon "Enjoy your stay!"

    # Background Inn Guest Hallway

    Stephy "Let's go to the beach after we unpack!"
    Leona "Sounds good!"

    # Background Inn Reception

    Daniel "Mr. Gordon? Besides the beach that we passed by on the way here, what other places are there to visit on this island?"
    Gordon "Well, there's a few gardens nearby that you can walk through, and there's a forest with hiking trails out back."
    Gordon "Although, if you plan to explore the woods, you'll have to sign some paperwork."
    Gordon "It's mainly things such as what time you'll leave, what time you plan to come back, and which trails you'll be travelling on."
    Gordon "Since it's hard to get a cellphone connection outside of the inn's Wi-Fi range, it's a safety precaution in case you get hurt or lost in the forest."
    Daniel "That makes sense. I guess we'll stick with the beach for today, then."
    Gordon "The beach is very nice at this time of year, it's a great place to spend your first day here."
    Gordon "You'll have to come back in pretty soon, though, there's a dinner party tonight to welcome all the guests."
    Daniel "I see, we'll make sure to make it back in time then."
    Daniel "Oh, they're here."

    # Foreground Stephy, Leona, Artin enter.

    Stephy "Let's go!"
    Gordon "Have fun out there!"

    # Background Pathway Along the Beach
    # Background The Beach (Day)
    # Foreground Daniel, Artin, Leona

    Daniel "It is a pretty nice beach."
    Artin "Yeah, the weather is good too-"
    Stephy "THE SEAAAAAAAAAAAAAAAAAAAAA!"
    Daniel "…"
    Artin "…"
    Leona "…"
    Leona "…should we help her up? Falling flat on her face like that has to hurt."
    Artin "Eh, the sand's soft enough."
    Artin "And I doubt it's affect her excitement in the least."
    Stephy "…*cough* *splutter* The seaaaaaaaaaaaa!…"
    Daniel "Doesn't this remind you of the first time we all met?"
    Artin "You mean the first year of high school when you and Stephy barged into the study room I was in?"
    Artin "She had failed a test by marking every answer as 'C'."
    Artin "And she genuinely believed every answer was 'C'!"
    Leona "Oh right…I was passing by when you guys opened the door and asked me to help convince her that you couldn't turn an angle into an acute angle by drawing smiley faces on them."
    Daniel "Yeah…"
    Daniel "I just had a sense of deja vu, you know?"

    #Foreground Claudine enters.

    Stranger "That girl that fell down earlier…is she okay?"
    Artin "Yeah, she's pretty much invincible when she gets excited."
    Stranger "…I…I see."
    Claudine "Ah, my name is Claudine. I'm sorry, I forgot to introduce myself back on the boat."
    Daniel "No worries! I'm Daniel, this is Artin, the frolicking one is Stephy, and the shy one here is Leona."
    Artin "Please don't take it personally, she gets a little nervous around strangers."
    Leona "…sorry…"
    Claudine "No, no, I understand. Sorry for troubling you."
    Claudine "Do you know about the dinner party tonight?"
    Daniel "Yes, we'll be heading back to the inn before it gets dark."
    Claudine "Alright. Stay safe, and keep an eye on that Stephy girl please."

    #Foreground Claudine leaves.

    Artin "I'm actually looking forward to dinner. Gordon's a pretty good chef."
    Artin "Although he tends to go a little heavy on the lamb sauce."

    #Background Inn Dining Hall (Night)
    #Foreground characters appear as they are called.

    Stephy "It's pretty fancy in here, with the candles"
    Stephy "And the food is delicious!"
    Leona "…are there seconds?"
    Daniel "Y-you polished off the entire plate already?!"
    Artin "Leona…that's not…"
    MrsWoodman "Don't worry, dear. I'm sure Gordon will be overjoyed to get you a second helping."
    MrWoodman "…"
    Bill "Hahaha! The little lady knows good food when she sees it!"
    Bill "Don't look so stern, Arthur! It's the highest compliment you can give to a chef!"
    Claudine "…be careful not to choke."
    Leona "…sorry…"
    Stephy "It's fine, Leona. The food is really, really tasty!"
    Gordon "And here's the next dish, baked cod with lemon and capers-"
    Gordon "Oh?"
    Daniel "?"
    Gordon "… … …ahahaha…"
    Gordon "Ahahahahaha! The promised challenger is finally here! Finally, the fruits of my labor…!"
    Leona "?"
    Gordon "I swear by my name and knives that I will meet- no, surpass your expectations!"
    Gordon "I'll be in the kitchen, please do not disturb me!"

    #Foreground: Gordon leaves.

    Leona "…? …??"
    Daniel "…Don't worry about it. I'm sure Gordon's planning to surprise us with an amazing dish."
    MrWoodman "…"
    Artin "…"
    MrsWoodman "…Dear…"
    Stephy "Thanks for letting us come on this trip, Mr. and Mrs. Woodman! It's been incredible so far!"
    MrWoodman "…"
    MrWoodman "You're welcome. I'm surprised that Artin's friends are so lively!"
    MrsWoodman "Has everyone here met each other already?"
    MrsWoodman "This is my son Artin, and his friends Daniel, Stephanie, and Leona."
    Stephy "You can call me Stephy!"
    MrsWoodman "This is Bill, one of my husband's business partners."
    Bill "Hahaha! Thanks for the introduction, Molly!"
    MrsWoodman "The elegant woman is Claudine, another guest that we met and befriended recently."
    Claudine "…"
    MrsWoodman "And in the corner over there is Maximilian. You needn't be so quiet, dear."
    Max "…"
    Leona "--!"
    Daniel "…Leona? What's wrong?"
    Gordon "As a slight change of plans, I have decided to skip over the beef bourguignon and present to you all my finest dish!"
    Gordon "A gracefully seared beef wellington with mushroom duxelles and English mustard, with a side of asparagus topped with hollandaise sauce, and garlic mashed potatoes!"

    #Foreground: Leona (eyes sparkling ver.)

    Leona "…!!"
    Bill "That looks amazing, Gordon old chap!"
    Daniel "W-Whoa…"
    MrsWoodman "You've really outdone yourself this time, Gordon!"
    Leona "…"
    Leona "…is there more?"
    Claudine "WHAT."
    Stephy "The normally-calm Claudine lost her cool!"
    Claudine "I didn't even see her fork! Did anyone see that?!"
    Gordon "… …hahaha…"
    Gordon "HAHAHAHAHAHA! I knew this battle wouldn't be so easily won! I shall return!"

    #Foreground: Gordon leaves.

    Artin "Leona… you really shouldn't eat so fast. It's not very polite…"
    MrWoodman "It's fine, Artin. I already know what kind of company you associate yourself with."
    Artin "--!"
    MrsWoodman "Dear, not now!"
    MrWoodman "…"
    Daniel "…"
    Artin "Please tell Gordon that dinner tonight was superb."
    MrWoodman "… Running away?"
    MrsWoodman "Dear!"
    Artin "…"

    #Foreground: Artin leaves.

    Stephy "…"
    Max "I'd like to call it a night as well. If you'll excuse me…"

    #Foreground: Max leaves.

    Daniel "Things turned sour rather quickly…"
    Leona "*munch* *chew*"
    Daniel "HEY! That's mine!"
    Leona "You weren't eating it…"
    Bill "Hahahah! Better watch your food, or the lion near you will snatch it up!"

    #Background: Daniel's Room

    Daniel "…"
    Daniel "I'm stuffed…"
    Daniel "Dinner was delicious, but I never did get to try that beef wellington…"
    Daniel "…"
    Daniel "I wonder what's up with Artin and his parents…"
    Daniel "Well, we'll worry about it in the morning."

    #Background: Daniel's Dream

    Stranger "…"
    Daniel "…"
    Daniel "It's strangely dark…"
    Daniel "But I can hear the sound of the waves…"
    Daniel "… …And now it's getting quieter…"
    Daniel "It almost feels like I'm sinking…"
    Stranger "…iel… …"
    Stranger "… … wa… up… … …ani… …"
    Stranger "… th… …ship … … Da… iel…"
    Daniel "Someone's voice? 'The ship'?"
    Stranger "Hello."
    Daniel "--!"
    Oz "You may call me Oz."
    Oz "There isn't much time left."
    Oz "Solve the boxes."
    Oz "They will grant you your wish."
    Daniel "…? My wish…?"
    Daniel "I don't understand…"
    Daniel "…"
    Daniel "…What a strange dream this is…"
    Oz "…It is."
    Oz "It truly is."

    #Background: fade to Black Screen
    #END OF CHAPTER 1.
    jump Chapter2


    # This ends the game.

    return

#!/usr/bin/env python3 
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Week 6 Assignment covering flow control
"""
#Please ignore any extra variables at the moment. This script is being designed to work both now and later.

print("""You are on an adventure, setting down an old dirt path on your trusty steed Zephyr.
After what seems to be an eternity you finally come to an intersection.
The path to the left ventures towards a forest grown thick with pines and moss.
The path in the center ahead leads to the foothills of the Seasky Mountains.
The path to the right points to a dried up riverbed that feeds into a murky swamp.

Zephyr is ready to ride with you wherever you choose. You are at the crossroads of your travels.

Which way do you go? Left, right, or center?""")

path = input("-> ")
middlepaths = ('middle', 'center', 'straight', 'ahead', 'forward', 'advance')
# == Left Path logic =======================
if path.lower() == "left":

    print("""Heading towards the forest the air cools around you but you feel the musty atmosphere in this dank realm.
Moss grows thick on the logs here, a low fog rolls over the ground.
After a while you start to notice that some of the stumps and logs are actually humanoid figures.
With limbs and heads and faces, you realize that these trees are not as you seem. Suddenly you see that you are
actually standing on the site of an ancient battle. Fallen warriors are strewn left and right in this graveyard.
On the peak of the battleground you see a slight glimmer. Between the trees the sun shines on a helmet perched
atop a sword driven into the ground. You can't help being attracted towards the helmet, it looks just your size..""")
    print("What do you do?\n")

    print("1. Hoist up the helm and wear it")
    print("2. Keep heading down the path")

    # == Forest logic ============================
    pathleft = input("-> ")

    if pathleft == "1":
        print("""You feel the power of the ancients flowing through your soul. Eons of knowledge are saturating your brain
and you can now feel the gravitational pull of the moon. Things are about to get interesting...

Stay tuned for Chapter 2!""")
        helmet = True
    elif pathleft == "2":   
        print("""This site only bares the truth to you, that some things are out of your control.
Maybe it is for the best that you keep heading on this path and see what lies beyond the forest.""")
        forestpath=1
    else:
        print(f"Make sure to choose valid answers next time, the story works better that way.")

# == Right Path Logic =====================
elif path.lower()  == "right":
    print("""The path leads down to an abandoned boat house and a dried up riverbed. It seems that at one point this
was a busy hub of trade and travel, with the river flowing from the Seasky Mountains out to the Lowland Channels.
It has been told that the Lowland Channels were once the home of a proud fishing tribe, but the river ceased to flow
and the channels dried up. Now it is a desolate swamp with no signs of life; any living beings have found new homes and
all that remains are scavengers and carrion. The boat house has fallen into disrepair but still stands, and its dock is
high above the muddy floor of the riverbed.""")
    print(f"What do you do?\n")
    print("1. Check out the boathouse for any signs of life.")
    print("2. Walk out the dock and think about what could have stopped the river's flow.")
    print("3. Begin your voyage into the swamp in search of life.")
    
    # == Swamp Logic ======================
    pathright = input("-> ")

    if pathright == "1" or pathright == "2":
        print("""The boathouse and dock are so old and rickety, you fear that the floorboards will collapse underneath you.
Very little evidence of life remains here, any leftover artifacts were stripped long ago by nomads and treasure hunters.
How this river could have dried up is a mystery, and it's hard to tell whether the answer lies upstream or down.""")
        print("Be ready to explore more in Chapter 2!")
    else:
        print("""There is nothing here for you now, and you feel the answer to this mystery lies within the swampy
remnants of the Lowland Channels. Whatever could have caused the river to dry up must have certainly been out of the 
control of the local tribe. They might have left with their boats before everything dried out, or they might have simply
moved on with their lives. There seems to be a boardwalk of sorts leading along the former shoreline, you decide to follow.""")
        print("To be continued in Chapter 2!")

# == Center Path Logic ========================
elif path.lower() in middlepaths:
    print("""This path leads you on a meandering climb up into the foothills of the Seasky Mountains. This side of
the mountain range has a gradual climb, in stark contrast to the sheer wall of the seaside slope. The mountains were named
such because of the way they stood in between the ocean and the horizon. Dangerous paths lead to the summits and certain doom lies
in wait for anyone that should venture carelessly.""")
    print("What do you do?\n")
    print("1) Press on towards the summit.")
    print("2) Head back to the crossroads.")

    #== Mountain Logic =======================
    pathmiddle = input("-> ")

    if pathmiddle == "1":
        print("""You decide to begin your ascent of the Seasky Mountains. It is unknown what perils you may face on this path,
but you think that there might be answers to be found. If you can keep your footing and survive the climb, you can be sure to discover
the secrets of the Seasky Mountains.""")

    else:
        print("""You decide that climbing up a dangerous mountain is not in your best interest. Perhaps heading back to the crossroad
will give you a fresh perspective.""")

# == Go Back Home Logic ======================
elif path.lower() == "back" or path.lower() == "go back" or path.lower() == "return":
    print("You have decided that adventuring is not for you today. Enjoy the rest of your days not knowing what was out there.")

else:
    print("You cannot decide where to go, so instead you decide to stay here. You are now the watchman of the crossroads.")

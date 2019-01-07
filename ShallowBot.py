import twitter, json, random, time, os
# Welcome to ShallowBot! 
# Github link > https://github.com/Shallowgam3r/Shallow-Bot
# Contact <<Shallowrobot@gmail.com>>   
# _*SLATT/!
lastMentionId = 0
settings = json.load(open('settings.json'))
if settings['use_env_variables']:
	api = twitter.Api(consumer_key = os.environ['consumer_key'], consumer_secret = os.environ['consumer_secret'], access_token_key = os.environ['access_token_key'], access_token_secret = os.environ['access_token_secret'])
	settings['account'] = os.environ['account']
	if os.environ['filter'] == 'true':
		settings['filter'] = True
	else:
		settings['filter'] = False
	settings['sleep_minutes'] = int(os.environ['sleep_minutes'])
else:
	auth = json.load(open('auth.json'))
	api = twitter.Api(consumer_key = auth['consumer_key'], consumer_secret = auth['consumer_secret'], access_token_key = auth['access_token_key'], access_token_secret = auth['access_token_secret'])

def constructTweet():
	tweetVocab = []
	tweetLength = 0
	tweetBody = ""
	for tweet in api.GetUserTimeline(screen_name = settings['account'], count = 1000): # Getting all the tweets from the account that will be imitated
		tweetWords = tweet.text.split(' ')
		for word in tweetWords: # Iterating over every word from each of the tweets
			if settings['filter'] and not word.startswith('@') and word.find('.') == -1: # Filtering out handles and links
				tweetVocab.append(word.replace('"', ' '))
	tweetLength = int(random.random() * 14)
	for x in range(0, tweetLength): # Choosing each of the words to use in the tweet
		if len(tweetBody) < 140: # Ensuring the tweet length is within it's limits
			tweetBody = tweetBody + tweetVocab[int(random.random() * len(tweetVocab))] + " "
		else: # If not, scrap the current tweet and start over
			tweetBody = ""
			constructTweet()
	if len(tweetBody) > 0:
		tweetBody = tweetBody.lower()
		api.PostUpdate(tweetBody) # Send the completed tweet onto twitter
		print("ShallowBot is functional! Tweet successfully posted!")

def checkMentions():
	global lastMentionId
	mentions = api.GetMentions(since_id=lastMentionId)
	if (len(mentions) > 0): # Checking if there's any unseen messages
		for mention in mentions: # If so, iterate over all of them
			api.PostUpdate("@" + mention.user.screen_name + " GOT MESSAGE", in_reply_to_status_id=mention.id)
	print(lastMentionId)

#if (len(api.GetMentions(since_id=lastMentionId, count=1)) > 0):
	#lastMentionId = api.GetMentions(since_id=lastMentionId, count=1)[0].id
print("ShallowBot is now running...")
#checkMentions()
#time.sleep(60)
#checkMentions()
while True: # The main loop to keep the program running
	constructTweet()
	time.sleep(60 * settings['sleep_minutes']) # Sleep to prevent API abuse

'''

																										 `    ` ``.....``  `                      ``   `   ```  `  `
																								`` `  `.:izxWWWWWWWWMz+;,.`   ``                 ` ``    `
																									`` ,#xxxnnznnznzzznnxxxn*, ``                 ``` .:;;;:.``
																								` .;xWnzzznzzzzzzznnzzzzznxMn;.               `.;+xMWWMMMWWMz+;.
																								`:xMnzzzzzzzzzznnzznzzzzzzznnxx*`        `  `,zxxxnnzzzzzznnnxMx*.`     `
																							`,nWzzzzzzzzzzzzzzzzzzzzzzzznnzznMn;`    `` .ixWnnnnnzzzzzzznnzzzzxW#:` `  `
																						``:nxznznzzzzzzzzzzzzzzzzzzzzzzznzzznx*`` ```;nxnzzzznnnnnzzzzznnzzzzzxMi``  `
																					 `.*WnzzznzzzzzzzzzzzzzzzzzzzzzznzznzzzzxM,`,iMxnzzzzzzznnnnzzzzzzzzznzzzzMM:``
																					 `zMzzzznznzzzzzzzzzzzzzzzzzzzzznnzznnzzzxx+xxzznzzznnzznnnzzzzzznnnnnzzznznx;``
																					.zMzznnnzznnzzzzzzzzzzzzzzzzzznnnzznzzzznznWnzzznnnnzzznzzzzzzzzznzzznznnznzzWi`
																				``zxznznznzzzzzzzzzzzzzznnzzzznnzzzzzzzzzzzzznMnzznnnnzzzzzzzzzzzzzzzznnnnnnnnzzM:
																			``.nxznzznzzzzzzzzzzzzzzzznnnnnnnnnzzzzzzzzzzzzzMMzznnnnnnzzzzzzzzzzzzzzzznnnnnzzznM.`
																			``zxzznznzzzzzzzzzzzzzzzzzznnnnzzznnnzzzzzzzzzzznWnznzznnnzzzzzzzzzzzzzzzznnnnzzzzzx+``
																			.+MznnnnnzzzzzzzzzzzzzzzzznnzzzznnzzzzzzzzzzzzzznnWnzzzznnzzzzzzzzzzzzzzzzzzzzzznznzx:  `
																			iMznznzzznzzzznzzzzzzzzzzzzznnnxxnnzzzzzzzzzzzzzzzWnzzzznnzzzzzzzzzzzzzzzzzzzzznznzzx#`
																`   `,WnzznzzzzzzznnnznzzzzzznxMMWWWWMMMWWWWMxnnzzzzznzzxWzzznnnnnnnnzzznnnnnnnnnnnnznnnzzzW`
																		`zxzzznzzzzznzznzzzzzznxWWxxnnzznzzzznnnxMWWxzzzzzzznWzznnnzzznnnnnnnnnnnnnnznnnnzzzzzzM;
																``  +MzzznzzzzzzzzzzzzznMWWMzznzzznnzzzzzzzzzzzzMWWxzznzzMnzznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzn#``
																	`.MzzznnzzzzzzzzzzzzMWMnzznzzzzznnnnzzzzzzznnzzzxWMnzznxMzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzn.
																	`#xzznnnzzzzzznzznMWxzznnzzznnnnnnznnnnznnzzznnnzzxWMnznWnzznnnxxxxMMMMWWWWWWWWWMMMMxxnnzzx,`
																 `:MzzznznzzzzzzzznMMnzzzzzzznnznzzzznzzzzzznnnzzzzzzzxWnzWxMMWWWWMMxxxxnnnnnnnnnnnnxxxMWWWMM*.`       `
																 `nnzzzzzznzzzzzznWnzzzzzzzzzzzzzzzzzzzzzzznnnzzzzzzzzznW@WMxnzzzzzzzzzzzzzzzzzzzzzzzzzzzzznxMWM+;````   `
																 .WnznzzzzzzzzzzznnnnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznMMzzznzzzzzzzzzzzzzzzzzzzzzznnnzzzzzzznxxni` `
																`#nznnzzzzzzzzzzznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznzzMWzzzzznzzzzzzzzzzzzzzzzzzzzzzzznnznzzzzzMn;``
																,xznznzzzzzzzzzzznnnnznnnnzzzzzzzzzzzzzzzzzzzzzzzznnnznzznzxMnnzzzzzzzzzzzzzzzzzzzzzznnnnnnnznnnzzzznx:`
																*xzzzzzzzzzzzzzzznnznnnnnnzzzzzznnzznnzzzzzzzzzzznnnnnzzzzzzxWxnnnznnznnznnzzzznzzzzzzzzzzzzzzzznznzzzMi`
															 `nxzzzzzzzzzzzzzzzzzzzzzzzzznnnnnnnnznzzzzzzzzznxMMMWWWWWWWMMxxWxzzzznzzznzzzzzzzzzzzzznnnnnnnnzzzznnzznM,`   `
														` `.WzzzzzzzzzzzzzzzzzzzzzzzzzzznnnnnzznzzznnxMMWWMMxnnnzzznnnnxMMWWMxnzznnzzzzznnnnxMMWWWWWWWWWWWWWWMMxxnzzx,`
															`ixnzzzzzzzzzzzzzzzzzzzzzzzzznzzzzznzzzxMWWMxxnzzzzzzzzzzzzznnzznnxWxznzznzzznMWWWxxxnnzzzzzzzzzzznnnxMWWWWn    `
															`znzzzznzzzzzzzzzzzzzzzznzzzzzzzzznnxWWMnzzzzzzzznnnnzzzzzznzzznzzzzMMzzzzxMWWxnzzzzzzzzzznnnnnnnnnnnzzzznxWx*.
														 `.xznznzzzzzzzzzzzzzzzzzzzzzzzzzzzzMWMxnnnzzzzzzzzzzzznnnnnnnzzzznzzzzWzzxMWxnzzzzzznxMMWWWWWWMMMMMMWWMnzzzzznM#, `
													```.ixzzzzzzzzzzzzzzzznzzzznnnzzzzzxWWxnzzzzzzzzzznnxxMWWWWMMMWWWWWMxxnzzxMWMnzzznnxMWWWMxnnzzzzzzzzzzzznxMWWMnzzznx.
											` ` `.*nMnzzzzzzzzzzzzzzzznnzzzzzzzzzxWMnnzzzznnzznxMWWWMxxxnznzzzzznnnxMWWMzxMnzznxWWMxxnzzzzznnnnzznnnzznzzzznnxWWnzzM;`
										 `` `:nWxzMnzzzzzzzzzzzzzzzzzznnnznnnxWMnzzzzzzznxMWWMxnzzzzzzzzzzzzzzzzzzz#nxWWnnMWWMnzzznnnnnzzzznnzznnnzznzzzzzzzzzMMxzz`
										 ```+xnz#nWzzzzzzzzzzzzzzzzzzzzznnnxWMnnzzzznxWWMxxnnnzzznnnnzzzzzzzzzzzzzzzzzznxMxnnzzznnzzzzzzzznnnnznzzzzzzzzzzzznnznMWx.
											,nxzzzzxxnzzzzzzzzzzzzzzzzznzxMWWMzzznnxMWWMnnzzzzzzznnnzznnnnnnnnnnnnnznnzzzz#zzzzzzzzzznzzzzzzzznnnxxMxxxxMMxxnnznznzzM+`
								`    `xxzzzzzMxzzzzzzzzzzzzzzzzzznznxnzznxMWMMnnnzzzzznzznnnnnnnzzzznnznzzzzzzzzzzzzzzzznnzzzznzzznzznxWWWx#+**;;ii*+#xWWxnzzzzM*``
										.zxznzznzWnzzzzzzzzzzzzzzzzzzznnxxMWWMnzzzznzzzzzzzzzznnznznzzzznnxxxxxxxxxxnnnnxWnzzznznnzzxxxxn#i:.``` ``.`.` ` ` ,i#xxnz#xz`
										*MznzznznWzzzzzzzzzzzzzzzzzzxMWWMxxnnnnnnnnnnnnzzzzznnnzzzzzznxWWWn+i;:,.,..`....*xnzzzzznWWn+;,.` `  ` :iznnn#:`   ` `,*nWxxz`
								 ` .WznzzznznWzzzzzzzzzzzzzzzzzz@xzzzznnnzznnnnznnnnnnzzzzzznnxMxn+i:,,,.`   ```     .Wzznxxn+,`  `  `  `:#@@@W@WWW@Mi`` ` `` .*M:`
									`+nznnnznnnWzzzzzzzzzzzzzzzzzzWznzzznzznnzzznnnzzzzzzzzznxWM+;i+nMMMMMn+, `         @MWni,``        ``zM@nW@W@WW@WWW;`    `` `+i
								 `:xzzznzzznnWzzzzzzzzzzzzzzzzzzWxznnzznznnznzznzzzznnxMxxzi..#@WM@WWWW@@@@z`         M*``            iW@W. .x@W@@WWWWWi `      .n  `
									+xnznzzzzznWzzzzzzzzzzzzzzzzzzxWnzzzzzzzzzznzznxMWWM#*:,` ix@M:,MWWWW@@WW@#`        n.          ` `:WW@M  `#W@@@W@WWWM`       `n``
								`.WnzznnzzzznxzzzzzzzzzzzzznzzzzznWMxxxxMMxxxxxn#*;,`` `  `+@WW;  ;@W@WWWW@@@n        x`         `  ,MW@W@;.;MWWMxM@WWW@i`    ` .n`
								`*xzzznzzzznznzzzzzzzzzzzzznnzzzzznxxxMxMWi:,,..`         iW@WWi  *W@W@@@@@WW@:`     :#`          ` #@@W@@MxM@WM,.:xWW@Mn`      ,z
								,xzznznzzzzzznzzzzzzzzzzzzznnnzznnzznzzzznM+. ``         `@WW@W@*+@W@W:.:nWW@Wn.    .n.  `         `@W@WWWWW@WW; ` i@@W@M:   ` .z;  `
								*xznznnzzzzzznznzzzzzzzzzzznnnzzzzzznznnzznMz, `       ` i@@WW@W@@WW@z ` :@WWWW:    *+  ``       ` ;WWW@W@@@WWW:  `;@@WWWi  ` ,zi``
							`.WnznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznzzzxW+,        `zWWWWWWWWW@W+ ` .@WW@Wz  .+W+ `  `      ``+WWWW@z`+WW@n.`,nW@WW@#.,+xM:
							`;MznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznznzznzznMxi`     `.xWWWWW@@@@@@n` `:@W@@@W :xMzMi.  ``   `   +WWW@W+`*@@WWn#x@W@W@WMnMxzx.
					 `  .nzznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnxnzzzzzMM*,` ` ,M@WWW@@:`M@W@n*+WWWWWW@MWzzzWMWz*,.``    `#W@@WW@W@W@W@@@@@WWWWMxz#znz`
					 `  ixzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznzznMWxzzzznnxM#i``,MWWWW@@i`WWWWW@@WW@@@MxnnzzxMzzxxxxz+i:,,:z@@WW@W@@@W@@WWMMxnnzzz##nW;`
						 `xnzzzznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnnznMWMxnzzzzxMWx+M@WWWWW@@@@@@@@WWMMnzzzzzzzMxzzzz#znxMMWWWMxxxMxxnxznzzzzzzznzzznxxz,
					 ``;MzznzznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznznzznnxMWMnzzzzznxMWW@@@@@WWMWMxxnnzzznnzzznMMznzzzzzzzzzzzzzzzzzzzzzzzzzzzzznznzzM*:`
						.zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznzzzzxMWWxnnnzzzzzzzzzzzzzzzzzzzzzzznnxWxzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnzzzx#`
					 `:MzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznzzznnnxxMMWWMxnnzzzzzzzzzzzzzznxMMWWMnnnzzzzzznnnnnnnnnnnnnnnnnnnnnzznnnznzx,`
						xnnnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznzznnzzzznxMMWWWMMMMMMMMWWWWWMxnnzzznzzzzzzznzznnzznnzznnzznnzznzznnnnznM,
					 ,WzznzzzznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnnzzzzzzznzzzznnnnnnnnnxxnnnnnzzzznznnzznnnnzzzzzzzzzzzzzzzzzzzzzzzznnnzM; `
					`znzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznzzzznnzznnnnzzznzzzznxxnzzzznzzzzznnzzzzzzzzzzzzzzzzznzzznzzzznx:
					:MznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnzznznnnnzzzxWMnnnzzzzzzzzznnzzzznnzzzzzzznnnnnzzzzzznMn:`
					nxznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnzzznxWWnnnnznzzzzzzzzxnnnnzznzzzzznnzzzznzzzznxx*`
				 ,WzzzznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznWWxnzznznzzzzzzznzMMMxzzzzzzzzzzzzzzznzznxM#,`
				.nznznznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznxWWnnzznzznzzzzzzzznznznMWxnzzzzzzzzznnxxMWWW*```
			 `;MzznnnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznxWWxnzzzzzzzzznzzzzzzzzzzzzxMWWMMMMMMWWWWMxnnnnM*``      `
			 .WzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnnnnzzxMWMnzzzzzzzzzzzzzzzzzzzzzzzzzzznM@MxxxnnnzzzzzzzzzM*`     `
		 ``*MzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzxWWxnzzznzzzzzzzzzzzzzzzzzzzzzzzzzzzxWMnzzznnnnzzzzzznM:`
			,xzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnznWWMnzzzznnnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzxzznnnnnnzzzzznzzW,`
			*xznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnxnnnnnzzzznzzzzzzzzzzzzzzzzzzzzzznzznzznzzzznnnnnzzzzzzzznz.
		 `MnzznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnnzzzzzzznnnnzzzzzzzzzzzzzzzzzzzzzzznnnnnznzznnzznnnzzzzzzzzzM#`
`    ;MzznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnzzzzzzznzznnzzzzzzzzzzzzzzzzzzzzzzzzzznnznznzzzzzzzzzzzzzznzzM,  `
		.znnnznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnznz. `
		,xznzznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnzzx:`
		ixzznznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnzznz`
		#nzznznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznzzznW. `
	` Mnznznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzx+`
	 `Wnzznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnzzznnnnnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznzzznzzn.
	 ,Wzznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnzzznnnnnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznzzznzzx:
	 :Mzznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznzzzznzzxi
	 ;Mzznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnzzzzzzx#
	 ixzznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnzzzznznn
	 ;MzznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznzzznxxMWWWWWWWWMMxxnnnzzzzzznnnzzzzznnnnnnnnnzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnnzznnnzznzznW`
	 ;WzznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznznWMxnnnnnnnnnnxxMMMMWMMxnnzzzzzzznzznnnnnnnznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznzzzxWW+` `
	 ,WzznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznMMnzznzzznnzzznzzzzzzznxMMWMxxnnzzznnzzznnnnnnzzzzzzzzzzznnnnzzzzzzzzzzzzzzzznznzznMWxzzx;` `
	 .WzznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzMMnnnnnnzzzzznnnnnnnnnnnnnnnnxMWWMxzzzzzzznnnznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznMWMxnnzznn
	 `WnzznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzxWzzzzzzznnnzzzzzzzzzzzzzzzznnzzznxMWWMxnnnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnxxWMxzzzzzznzW`
	` nnznznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznzzznWnnnzzzzzzznzzzzzzzzzzznnnzznnnznzzznnxMMWWMMxnzzzzzzzzznnnzzzzznnzzzzzzznxMWWMxnnznzznnznnW`
		*nznzznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznznznWnnzzznnnnnnnxxxxxxxxnzzzzznzzzzzznnnnzzzznnxMWWWWMMxxxxxnnnnnnnxxxxxMMWWMMxnzzzzzzzznzznzxz
		:xzznznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnznWnnzzznxWWWMMMxxxMMMWWWMxnnzzzzznzzzzznnnzznnnnnnnnxxxxMMMMMMMMMMxxxxxnnznnzzzznzzzzznznnzM;  `
		.nzznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnznWnnzznnnnzzzzzzzzzzzzzznxMMMMxnnzzzznzznnnnnnznznnnnnzzzzzzzzzzzzzznnznnnnnnzzznznzzzzznnMi`  `
		`*xzzznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnnznMnzzzznnnzzzzzzzzzzzzzzzzznnxMMWMxnzzzzzznnzzzzzzzznnnnnnzzzzzzzzzzznzznnzznzzzzzzzzzzznx+
 `   .MnzznzzzzzzzzzzzzzzzzzzzzzzzzzznnnznnnnnznWnzzzznzznnnnnnznnnnzzzzzzznzzzznxWWMMxxnnnnnzzznnnnznnznzzzzzzzzzzzzzzzznnnnnnnnnnnnnxn, `
		 `#xnnzzzzzzzzzznzzzzzzzzzzzzzzzznnznnzzzzzzWnzznzzznnnzzzzznzzzzzzzzzzzzzzzzznnnxxMMWMMxnnzzzznnzzzznnnnnnnzzzzznnnzzznnnxxMMMMMW+.
			,xzzzzzzzzzzzzzzzzzzzzzzzzzzzzznzznzzzzzzzMxzzznnnnnznzzzznnzznnznzzznnnnnnnnnnnnzzzznxMMWMMMxxxxxxxnnnnnnxxxxxxMMMMWWWMxxnnnzzx+`  `
			`#nzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnznzzzzzxWxnnnzzzzzzzzzzzzzzzzzzzzznnnnnzzznnzzzzzzzznnnnnnnxxxxxxxMMMMMxxxxxxxnnnnzzzzzzzzzzn+`
			 .MnzzzznnzzzzzzzzzzzzzzzzzzzzzznzxWzzzzzznnMWWWWMMMMxxxxxnnnzzzzzzzznnnnnzznnnnnnnnnzzzzzzzznnnnnnnnnnnnnzzzzznnzzzznnzzznzzzzx*`  `
			``*xzzzznnnzzzzzzzzzzzzzzzzzzzzzzznWnzzzzzzznzzznnnnnxxMMMWWWMxnnzzzzzzzzzzzzzznnnnznnnzzznnnzzznnnnnnnnnnnnnnnzzznnnzzznnzzzznMi
			 ``#nznznnnnzzzzzzzzzzzzzzzzzzznzzzxMnnnzznzzzzzzzzzzzzzzzzznxMMWWMMxxnnnnzzzzzznzzzzzzzzznzzzzzzzzzzzzzzzzzzzzzzzzzzznnnnznzznW.` `
				 .MxznznnnzzzzzzzzzzzzzzzzzzzzznznMxzn#nznnnnnzzzzzzzzzzzzzzzznnnxxMMWMMxnzzzzznnzznzzzzzzzzzzznnnnzznnnzzzzzzzzzzzzzzznnnznnx` `
			`  `:xnzznznzzzzzzzzzzzzzzzzzzznzznznWxznzzzzzzzzzzzznnnnnzzzzzzznnnnzzznxxMWWWMMxxxxnnnnnnnnzzzzznnnnzzzzzzzzzznnnnnnnnnnzzznx: `
					`:WzzzzzzzzzzzzzzzzzzzzzzzznnnzzznWMzznnnnnnzzzzznnnnnzznnnnnnzzzzzzzzzzznnnxxxMMWWWMMxxnnnnnzzzzzzzznnnnnnnnnnnnnzznnzznW;`  `
			 ` ```;xnnzzzzzzzzzzzzzzzzzzzzzznnznnzzxWMnnnnzzzzzzznnnnnnnzzzzzzzznnnzzzzzzzzzzzzzzzznnxxxMWWWWWWMMMMMMMMMMMMxxxxxxxxxxxxx#.`
					 ``:WxzznnzznnnznzzzzzzzzznnnnnnzzzzxxMWMnnzzzzzzzzznnzzznnnnnnnzzzzzzzzzzzzzzzznzzzzzzzzzzzznnnnnnnnnxxxxxxxxxxWM**ii:,`
						``:zxzzzznzznzzzzzzzzzzzznnnnnnzzzzzznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnzzxz,
					 `  `.zMnzznzznnzzzzzzzzzzzzzzzzzzzzzznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnnnnzMz.
							```,nxnzznznzzzzzzzzzzzzzzzzzzzzzzzznnnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnnznnznM*.
							````.iMMzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnnnnznnzzxMi`
									` `;xMnzzzzzznnnnnznnnzzzzzzzznnnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnzznnnzzznznM#`` `
										 `.;xWxzznzznnnznnnnnnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnzznnnzzzzzxW;`
											 ``,+xxnnzzzzznnnnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnnnzznznMMi``
												 ``,i#MWnnzzzzznzznzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnzzzzzzzxW+:``
														 ``,*zxxxxnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznnzznMx*. ` `
																``.:*#xWWxnzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzznzznMWxi,   ` `
																			 `:*zxxnxxnnzzzzzzzzzzzzznnnzzzzzznnnnnnnnzzznnnnnnnnnnnnzzzzznxxxz*.
																		 ``   `.,;i*nMWWMxnzzzzzzzzzzzzzzzzznnnzzzzzzzzzzzzzzzzzzzzznxMWx#;,``
																							 ````,;i+zxxnxxxxxxnnnnnnzzzzzzzzzzzzzzznnnnxxxxxxz*:.`
																								``   ```..,:;i*+#znxMMMWWWWWWWWWWWWWWWMxnz+i;:,.`
																																		 ```..,.....,...``     ``
'''

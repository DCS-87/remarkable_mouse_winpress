# generated by generate_codes.py

types= {0: 'EV_SYN',
 1: 'EV_KEY',
 2: 'EV_REL',
 3: 'EV_ABS',
 4: 'EV_MSC',
 5: 'EV_SW',
 17: 'EV_LED',
 18: 'EV_SND',
 20: 'EV_REP',
 21: 'EV_FF',
 22: 'EV_PWR',
 23: 'EV_FF_STATUS',
 31: 'EV_MAX'}
codes = {0: {0: 'SYN_REPORT',
     1: 'SYN_CONFIG',
     2: 'SYN_MT_REPORT',
     3: 'SYN_DROPPED',
     4: 'SYN_04',
     5: 'SYN_05',
     6: 'SYN_06',
     7: 'SYN_07',
     8: 'SYN_08',
     9: 'SYN_09',
     10: 'SYN_0A',
     11: 'SYN_0B',
     12: 'SYN_0C',
     13: 'SYN_0D',
     14: 'SYN_0E',
     15: 'SYN_MAX'},
 1: {0: 'KEY_RESERVED',
     1: 'KEY_ESC',
     2: 'KEY_1',
     3: 'KEY_2',
     4: 'KEY_3',
     5: 'KEY_4',
     6: 'KEY_5',
     7: 'KEY_6',
     8: 'KEY_7',
     9: 'KEY_8',
     10: 'KEY_9',
     11: 'KEY_0',
     12: 'KEY_MINUS',
     13: 'KEY_EQUAL',
     14: 'KEY_BACKSPACE',
     15: 'KEY_TAB',
     16: 'KEY_Q',
     17: 'KEY_W',
     18: 'KEY_E',
     19: 'KEY_R',
     20: 'KEY_T',
     21: 'KEY_Y',
     22: 'KEY_U',
     23: 'KEY_I',
     24: 'KEY_O',
     25: 'KEY_P',
     26: 'KEY_LEFTBRACE',
     27: 'KEY_RIGHTBRACE',
     28: 'KEY_ENTER',
     29: 'KEY_LEFTCTRL',
     30: 'KEY_A',
     31: 'KEY_S',
     32: 'KEY_D',
     33: 'KEY_F',
     34: 'KEY_G',
     35: 'KEY_H',
     36: 'KEY_J',
     37: 'KEY_K',
     38: 'KEY_L',
     39: 'KEY_SEMICOLON',
     40: 'KEY_APOSTROPHE',
     41: 'KEY_GRAVE',
     42: 'KEY_LEFTSHIFT',
     43: 'KEY_BACKSLASH',
     44: 'KEY_Z',
     45: 'KEY_X',
     46: 'KEY_C',
     47: 'KEY_V',
     48: 'KEY_B',
     49: 'KEY_N',
     50: 'KEY_M',
     51: 'KEY_COMMA',
     52: 'KEY_DOT',
     53: 'KEY_SLASH',
     54: 'KEY_RIGHTSHIFT',
     55: 'KEY_KPASTERISK',
     56: 'KEY_LEFTALT',
     57: 'KEY_SPACE',
     58: 'KEY_CAPSLOCK',
     59: 'KEY_F1',
     60: 'KEY_F2',
     61: 'KEY_F3',
     62: 'KEY_F4',
     63: 'KEY_F5',
     64: 'KEY_F6',
     65: 'KEY_F7',
     66: 'KEY_F8',
     67: 'KEY_F9',
     68: 'KEY_F10',
     69: 'KEY_NUMLOCK',
     70: 'KEY_SCROLLLOCK',
     71: 'KEY_KP7',
     72: 'KEY_KP8',
     73: 'KEY_KP9',
     74: 'KEY_KPMINUS',
     75: 'KEY_KP4',
     76: 'KEY_KP5',
     77: 'KEY_KP6',
     78: 'KEY_KPPLUS',
     79: 'KEY_KP1',
     80: 'KEY_KP2',
     81: 'KEY_KP3',
     82: 'KEY_KP0',
     83: 'KEY_KPDOT',
     84: 'KEY_54',
     85: 'KEY_ZENKAKUHANKAKU',
     86: 'KEY_102ND',
     87: 'KEY_F11',
     88: 'KEY_F12',
     89: 'KEY_RO',
     90: 'KEY_KATAKANA',
     91: 'KEY_HIRAGANA',
     92: 'KEY_HENKAN',
     93: 'KEY_KATAKANAHIRAGANA',
     94: 'KEY_MUHENKAN',
     95: 'KEY_KPJPCOMMA',
     96: 'KEY_KPENTER',
     97: 'KEY_RIGHTCTRL',
     98: 'KEY_KPSLASH',
     99: 'KEY_SYSRQ',
     100: 'KEY_RIGHTALT',
     101: 'KEY_LINEFEED',
     102: 'KEY_HOME',
     103: 'KEY_UP',
     104: 'KEY_PAGEUP',
     105: 'KEY_LEFT',
     106: 'KEY_RIGHT',
     107: 'KEY_END',
     108: 'KEY_DOWN',
     109: 'KEY_PAGEDOWN',
     110: 'KEY_INSERT',
     111: 'KEY_DELETE',
     112: 'KEY_MACRO',
     113: 'KEY_MUTE',
     114: 'KEY_VOLUMEDOWN',
     115: 'KEY_VOLUMEUP',
     116: 'KEY_POWER',
     117: 'KEY_KPEQUAL',
     118: 'KEY_KPPLUSMINUS',
     119: 'KEY_PAUSE',
     120: 'KEY_SCALE',
     121: 'KEY_KPCOMMA',
     122: 'KEY_HANGEUL',
     123: 'KEY_HANJA',
     124: 'KEY_YEN',
     125: 'KEY_LEFTMETA',
     126: 'KEY_RIGHTMETA',
     127: 'KEY_COMPOSE',
     128: 'KEY_STOP',
     129: 'KEY_AGAIN',
     130: 'KEY_PROPS',
     131: 'KEY_UNDO',
     132: 'KEY_FRONT',
     133: 'KEY_COPY',
     134: 'KEY_OPEN',
     135: 'KEY_PASTE',
     136: 'KEY_FIND',
     137: 'KEY_CUT',
     138: 'KEY_HELP',
     139: 'KEY_MENU',
     140: 'KEY_CALC',
     141: 'KEY_SETUP',
     142: 'KEY_SLEEP',
     143: 'KEY_WAKEUP',
     144: 'KEY_FILE',
     145: 'KEY_SENDFILE',
     146: 'KEY_DELETEFILE',
     147: 'KEY_XFER',
     148: 'KEY_PROG1',
     149: 'KEY_PROG2',
     150: 'KEY_WWW',
     151: 'KEY_MSDOS',
     152: 'KEY_COFFEE',
     153: 'KEY_ROTATE_DISPLAY',
     154: 'KEY_CYCLEWINDOWS',
     155: 'KEY_MAIL',
     156: 'KEY_BOOKMARKS',
     157: 'KEY_COMPUTER',
     158: 'KEY_BACK',
     159: 'KEY_FORWARD',
     160: 'KEY_CLOSECD',
     161: 'KEY_EJECTCD',
     162: 'KEY_EJECTCLOSECD',
     163: 'KEY_NEXTSONG',
     164: 'KEY_PLAYPAUSE',
     165: 'KEY_PREVIOUSSONG',
     166: 'KEY_STOPCD',
     167: 'KEY_RECORD',
     168: 'KEY_REWIND',
     169: 'KEY_PHONE',
     170: 'KEY_ISO',
     171: 'KEY_CONFIG',
     172: 'KEY_HOMEPAGE',
     173: 'KEY_REFRESH',
     174: 'KEY_EXIT',
     175: 'KEY_MOVE',
     176: 'KEY_EDIT',
     177: 'KEY_SCROLLUP',
     178: 'KEY_SCROLLDOWN',
     179: 'KEY_KPLEFTPAREN',
     180: 'KEY_KPRIGHTPAREN',
     181: 'KEY_NEW',
     182: 'KEY_REDO',
     183: 'KEY_F13',
     184: 'KEY_F14',
     185: 'KEY_F15',
     186: 'KEY_F16',
     187: 'KEY_F17',
     188: 'KEY_F18',
     189: 'KEY_F19',
     190: 'KEY_F20',
     191: 'KEY_F21',
     192: 'KEY_F22',
     193: 'KEY_F23',
     194: 'KEY_F24',
     195: 'KEY_C3',
     196: 'KEY_C4',
     197: 'KEY_C5',
     198: 'KEY_C6',
     199: 'KEY_C7',
     200: 'KEY_PLAYCD',
     201: 'KEY_PAUSECD',
     202: 'KEY_PROG3',
     203: 'KEY_PROG4',
     204: 'KEY_DASHBOARD',
     205: 'KEY_SUSPEND',
     206: 'KEY_CLOSE',
     207: 'KEY_PLAY',
     208: 'KEY_FASTFORWARD',
     209: 'KEY_BASSBOOST',
     210: 'KEY_PRINT',
     211: 'KEY_HP',
     212: 'KEY_CAMERA',
     213: 'KEY_SOUND',
     214: 'KEY_QUESTION',
     215: 'KEY_EMAIL',
     216: 'KEY_CHAT',
     217: 'KEY_SEARCH',
     218: 'KEY_CONNECT',
     219: 'KEY_FINANCE',
     220: 'KEY_SPORT',
     221: 'KEY_SHOP',
     222: 'KEY_ALTERASE',
     223: 'KEY_CANCEL',
     224: 'KEY_BRIGHTNESSDOWN',
     225: 'KEY_BRIGHTNESSUP',
     226: 'KEY_MEDIA',
     227: 'KEY_SWITCHVIDEOMODE',
     228: 'KEY_KBDILLUMTOGGLE',
     229: 'KEY_KBDILLUMDOWN',
     230: 'KEY_KBDILLUMUP',
     231: 'KEY_SEND',
     232: 'KEY_REPLY',
     233: 'KEY_FORWARDMAIL',
     234: 'KEY_SAVE',
     235: 'KEY_DOCUMENTS',
     236: 'KEY_BATTERY',
     237: 'KEY_BLUETOOTH',
     238: 'KEY_WLAN',
     239: 'KEY_UWB',
     240: 'KEY_UNKNOWN',
     241: 'KEY_VIDEO_NEXT',
     242: 'KEY_VIDEO_PREV',
     243: 'KEY_BRIGHTNESS_CYCLE',
     244: 'KEY_BRIGHTNESS_AUTO',
     245: 'KEY_DISPLAY_OFF',
     246: 'KEY_WWAN',
     247: 'KEY_RFKILL',
     248: 'KEY_MICMUTE',
     249: 'KEY_F9',
     250: 'KEY_FA',
     251: 'KEY_FB',
     252: 'KEY_FC',
     253: 'KEY_FD',
     254: 'KEY_FE',
     255: 'KEY_FF',
     256: 'BTN_0',
     257: 'BTN_1',
     258: 'BTN_2',
     259: 'BTN_3',
     260: 'BTN_4',
     261: 'BTN_5',
     262: 'BTN_6',
     263: 'BTN_7',
     264: 'BTN_8',
     265: 'BTN_9',
     266: 'KEY_10A',
     267: 'KEY_10B',
     268: 'KEY_10C',
     269: 'KEY_10D',
     270: 'KEY_10E',
     271: 'KEY_10F',
     272: 'BTN_LEFT',
     273: 'BTN_RIGHT',
     274: 'BTN_MIDDLE',
     275: 'BTN_SIDE',
     276: 'BTN_EXTRA',
     277: 'BTN_FORWARD',
     278: 'BTN_BACK',
     279: 'BTN_TASK',
     280: 'KEY_118',
     281: 'KEY_119',
     282: 'KEY_11A',
     283: 'KEY_11B',
     284: 'KEY_11C',
     285: 'KEY_11D',
     286: 'KEY_11E',
     287: 'KEY_11F',
     288: 'BTN_TRIGGER',
     289: 'BTN_THUMB',
     290: 'BTN_THUMB2',
     291: 'BTN_TOP',
     292: 'BTN_TOP2',
     293: 'BTN_PINKIE',
     294: 'BTN_BASE',
     295: 'BTN_BASE2',
     296: 'BTN_BASE3',
     297: 'BTN_BASE4',
     298: 'BTN_BASE5',
     299: 'BTN_BASE6',
     300: 'KEY_12C',
     301: 'KEY_12D',
     302: 'KEY_12E',
     303: 'BTN_DEAD',
     304: 'BTN_SOUTH',
     305: 'BTN_EAST',
     306: 'BTN_C',
     307: 'BTN_NORTH',
     308: 'BTN_WEST',
     309: 'BTN_Z',
     310: 'BTN_TL',
     311: 'BTN_TR',
     312: 'BTN_TL2',
     313: 'BTN_TR2',
     314: 'BTN_SELECT',
     315: 'BTN_START',
     316: 'BTN_MODE',
     317: 'BTN_THUMBL',
     318: 'BTN_THUMBR',
     319: 'KEY_13F',
     320: 'BTN_TOOL_PEN',
     321: 'BTN_TOOL_RUBBER',
     322: 'BTN_TOOL_BRUSH',
     323: 'BTN_TOOL_PENCIL',
     324: 'BTN_TOOL_AIRBRUSH',
     325: 'BTN_TOOL_FINGER',
     326: 'BTN_TOOL_MOUSE',
     327: 'BTN_TOOL_LENS',
     328: 'BTN_TOOL_QUINTTAP',
     329: 'BTN_STYLUS3',
     330: 'BTN_TOUCH',
     331: 'BTN_STYLUS',
     332: 'BTN_STYLUS2',
     333: 'BTN_TOOL_DOUBLETAP',
     334: 'BTN_TOOL_TRIPLETAP',
     335: 'BTN_TOOL_QUADTAP',
     336: 'BTN_GEAR_DOWN',
     337: 'BTN_GEAR_UP',
     338: 'KEY_152',
     339: 'KEY_153',
     340: 'KEY_154',
     341: 'KEY_155',
     342: 'KEY_156',
     343: 'KEY_157',
     344: 'KEY_158',
     345: 'KEY_159',
     346: 'KEY_15A',
     347: 'KEY_15B',
     348: 'KEY_15C',
     349: 'KEY_15D',
     350: 'KEY_15E',
     351: 'KEY_15F',
     352: 'KEY_OK',
     353: 'KEY_SELECT',
     354: 'KEY_GOTO',
     355: 'KEY_CLEAR',
     356: 'KEY_POWER2',
     357: 'KEY_OPTION',
     358: 'KEY_INFO',
     359: 'KEY_TIME',
     360: 'KEY_VENDOR',
     361: 'KEY_ARCHIVE',
     362: 'KEY_PROGRAM',
     363: 'KEY_CHANNEL',
     364: 'KEY_FAVORITES',
     365: 'KEY_EPG',
     366: 'KEY_PVR',
     367: 'KEY_MHP',
     368: 'KEY_LANGUAGE',
     369: 'KEY_TITLE',
     370: 'KEY_SUBTITLE',
     371: 'KEY_ANGLE',
     372: 'KEY_FULL_SCREEN',
     373: 'KEY_MODE',
     374: 'KEY_KEYBOARD',
     375: 'KEY_ASPECT_RATIO',
     376: 'KEY_PC',
     377: 'KEY_TV',
     378: 'KEY_TV2',
     379: 'KEY_VCR',
     380: 'KEY_VCR2',
     381: 'KEY_SAT',
     382: 'KEY_SAT2',
     383: 'KEY_CD',
     384: 'KEY_TAPE',
     385: 'KEY_RADIO',
     386: 'KEY_TUNER',
     387: 'KEY_PLAYER',
     388: 'KEY_TEXT',
     389: 'KEY_DVD',
     390: 'KEY_AUX',
     391: 'KEY_MP3',
     392: 'KEY_AUDIO',
     393: 'KEY_VIDEO',
     394: 'KEY_DIRECTORY',
     395: 'KEY_LIST',
     396: 'KEY_MEMO',
     397: 'KEY_CALENDAR',
     398: 'KEY_RED',
     399: 'KEY_GREEN',
     400: 'KEY_YELLOW',
     401: 'KEY_BLUE',
     402: 'KEY_CHANNELUP',
     403: 'KEY_CHANNELDOWN',
     404: 'KEY_FIRST',
     405: 'KEY_LAST',
     406: 'KEY_AB',
     407: 'KEY_NEXT',
     408: 'KEY_RESTART',
     409: 'KEY_SLOW',
     410: 'KEY_SHUFFLE',
     411: 'KEY_BREAK',
     412: 'KEY_PREVIOUS',
     413: 'KEY_DIGITS',
     414: 'KEY_TEEN',
     415: 'KEY_TWEN',
     416: 'KEY_VIDEOPHONE',
     417: 'KEY_GAMES',
     418: 'KEY_ZOOMIN',
     419: 'KEY_ZOOMOUT',
     420: 'KEY_ZOOMRESET',
     421: 'KEY_WORDPROCESSOR',
     422: 'KEY_EDITOR',
     423: 'KEY_SPREADSHEET',
     424: 'KEY_GRAPHICSEDITOR',
     425: 'KEY_PRESENTATION',
     426: 'KEY_DATABASE',
     427: 'KEY_NEWS',
     428: 'KEY_VOICEMAIL',
     429: 'KEY_ADDRESSBOOK',
     430: 'KEY_MESSENGER',
     431: 'KEY_DISPLAYTOGGLE',
     432: 'KEY_SPELLCHECK',
     433: 'KEY_LOGOFF',
     434: 'KEY_DOLLAR',
     435: 'KEY_EURO',
     436: 'KEY_FRAMEBACK',
     437: 'KEY_FRAMEFORWARD',
     438: 'KEY_CONTEXT_MENU',
     439: 'KEY_MEDIA_REPEAT',
     440: 'KEY_10CHANNELSUP',
     441: 'KEY_10CHANNELSDOWN',
     442: 'KEY_IMAGES',
     443: 'KEY_1BB',
     444: 'KEY_NOTIFICATION_CENTER',
     445: 'KEY_PICKUP_PHONE',
     446: 'KEY_HANGUP_PHONE',
     447: 'KEY_1BF',
     448: 'KEY_DEL_EOL',
     449: 'KEY_DEL_EOS',
     450: 'KEY_INS_LINE',
     451: 'KEY_DEL_LINE',
     452: 'KEY_1C4',
     453: 'KEY_1C5',
     454: 'KEY_1C6',
     455: 'KEY_1C7',
     456: 'KEY_1C8',
     457: 'KEY_1C9',
     458: 'KEY_1CA',
     459: 'KEY_1CB',
     460: 'KEY_1CC',
     461: 'KEY_1CD',
     462: 'KEY_1CE',
     463: 'KEY_1CF',
     464: 'KEY_FN',
     465: 'KEY_FN_ESC',
     466: 'KEY_FN_F1',
     467: 'KEY_FN_F2',
     468: 'KEY_FN_F3',
     469: 'KEY_FN_F4',
     470: 'KEY_FN_F5',
     471: 'KEY_FN_F6',
     472: 'KEY_FN_F7',
     473: 'KEY_FN_F8',
     474: 'KEY_FN_F9',
     475: 'KEY_FN_F10',
     476: 'KEY_FN_F11',
     477: 'KEY_FN_F12',
     478: 'KEY_FN_1',
     479: 'KEY_FN_2',
     480: 'KEY_FN_D',
     481: 'KEY_FN_E',
     482: 'KEY_FN_F',
     483: 'KEY_FN_S',
     484: 'KEY_FN_B',
     485: 'KEY_FN_RIGHT_SHIFT',
     486: 'KEY_1E6',
     487: 'KEY_1E7',
     488: 'KEY_1E8',
     489: 'KEY_1E9',
     490: 'KEY_1EA',
     491: 'KEY_1EB',
     492: 'KEY_1EC',
     493: 'KEY_1ED',
     494: 'KEY_1EE',
     495: 'KEY_1EF',
     496: 'KEY_1F0',
     497: 'KEY_BRL_DOT1',
     498: 'KEY_BRL_DOT2',
     499: 'KEY_BRL_DOT3',
     500: 'KEY_BRL_DOT4',
     501: 'KEY_BRL_DOT5',
     502: 'KEY_BRL_DOT6',
     503: 'KEY_BRL_DOT7',
     504: 'KEY_BRL_DOT8',
     505: 'KEY_BRL_DOT9',
     506: 'KEY_BRL_DOT10',
     507: 'KEY_1FB',
     508: 'KEY_1FC',
     509: 'KEY_1FD',
     510: 'KEY_1FE',
     511: 'KEY_1FF',
     512: 'KEY_NUMERIC_0',
     513: 'KEY_NUMERIC_1',
     514: 'KEY_NUMERIC_2',
     515: 'KEY_NUMERIC_3',
     516: 'KEY_NUMERIC_4',
     517: 'KEY_NUMERIC_5',
     518: 'KEY_NUMERIC_6',
     519: 'KEY_NUMERIC_7',
     520: 'KEY_NUMERIC_8',
     521: 'KEY_NUMERIC_9',
     522: 'KEY_NUMERIC_STAR',
     523: 'KEY_NUMERIC_POUND',
     524: 'KEY_NUMERIC_A',
     525: 'KEY_NUMERIC_B',
     526: 'KEY_NUMERIC_C',
     527: 'KEY_NUMERIC_D',
     528: 'KEY_CAMERA_FOCUS',
     529: 'KEY_WPS_BUTTON',
     530: 'KEY_TOUCHPAD_TOGGLE',
     531: 'KEY_TOUCHPAD_ON',
     532: 'KEY_TOUCHPAD_OFF',
     533: 'KEY_CAMERA_ZOOMIN',
     534: 'KEY_CAMERA_ZOOMOUT',
     535: 'KEY_CAMERA_UP',
     536: 'KEY_CAMERA_DOWN',
     537: 'KEY_CAMERA_LEFT',
     538: 'KEY_CAMERA_RIGHT',
     539: 'KEY_ATTENDANT_ON',
     540: 'KEY_ATTENDANT_OFF',
     541: 'KEY_ATTENDANT_TOGGLE',
     542: 'KEY_LIGHTS_TOGGLE',
     543: 'KEY_21F',
     544: 'BTN_DPAD_UP',
     545: 'BTN_DPAD_DOWN',
     546: 'BTN_DPAD_LEFT',
     547: 'BTN_DPAD_RIGHT',
     548: 'KEY_224',
     549: 'KEY_225',
     550: 'KEY_226',
     551: 'KEY_227',
     552: 'KEY_228',
     553: 'KEY_229',
     554: 'KEY_22A',
     555: 'KEY_22B',
     556: 'KEY_22C',
     557: 'KEY_22D',
     558: 'KEY_22E',
     559: 'KEY_22F',
     560: 'KEY_ALS_TOGGLE',
     561: 'KEY_ROTATE_LOCK_TOGGLE',
     562: 'KEY_232',
     563: 'KEY_233',
     564: 'KEY_234',
     565: 'KEY_235',
     566: 'KEY_236',
     567: 'KEY_237',
     568: 'KEY_238',
     569: 'KEY_239',
     570: 'KEY_23A',
     571: 'KEY_23B',
     572: 'KEY_23C',
     573: 'KEY_23D',
     574: 'KEY_23E',
     575: 'KEY_23F',
     576: 'KEY_BUTTONCONFIG',
     577: 'KEY_TASKMANAGER',
     578: 'KEY_JOURNAL',
     579: 'KEY_CONTROLPANEL',
     580: 'KEY_APPSELECT',
     581: 'KEY_SCREENSAVER',
     582: 'KEY_VOICECOMMAND',
     583: 'KEY_ASSISTANT',
     584: 'KEY_KBD_LAYOUT_NEXT',
     585: 'KEY_EMOJI_PICKER',
     586: 'KEY_24A',
     587: 'KEY_24B',
     588: 'KEY_24C',
     589: 'KEY_24D',
     590: 'KEY_24E',
     591: 'KEY_24F',
     592: 'KEY_BRIGHTNESS_MIN',
     593: 'KEY_BRIGHTNESS_MAX',
     594: 'KEY_252',
     595: 'KEY_253',
     596: 'KEY_254',
     597: 'KEY_255',
     598: 'KEY_256',
     599: 'KEY_257',
     600: 'KEY_258',
     601: 'KEY_259',
     602: 'KEY_25A',
     603: 'KEY_25B',
     604: 'KEY_25C',
     605: 'KEY_25D',
     606: 'KEY_25E',
     607: 'KEY_25F',
     608: 'KEY_KBDINPUTASSIST_PREV',
     609: 'KEY_KBDINPUTASSIST_NEXT',
     610: 'KEY_KBDINPUTASSIST_PREVGROUP',
     611: 'KEY_KBDINPUTASSIST_NEXTGROUP',
     612: 'KEY_KBDINPUTASSIST_ACCEPT',
     613: 'KEY_KBDINPUTASSIST_CANCEL',
     614: 'KEY_RIGHT_UP',
     615: 'KEY_RIGHT_DOWN',
     616: 'KEY_LEFT_UP',
     617: 'KEY_LEFT_DOWN',
     618: 'KEY_ROOT_MENU',
     619: 'KEY_MEDIA_TOP_MENU',
     620: 'KEY_NUMERIC_11',
     621: 'KEY_NUMERIC_12',
     622: 'KEY_AUDIO_DESC',
     623: 'KEY_3D_MODE',
     624: 'KEY_NEXT_FAVORITE',
     625: 'KEY_STOP_RECORD',
     626: 'KEY_PAUSE_RECORD',
     627: 'KEY_VOD',
     628: 'KEY_UNMUTE',
     629: 'KEY_FASTREVERSE',
     630: 'KEY_SLOWREVERSE',
     631: 'KEY_DATA',
     632: 'KEY_ONSCREEN_KEYBOARD',
     633: 'KEY_PRIVACY_SCREEN_TOGGLE',
     634: 'KEY_SELECTIVE_SCREENSHOT',
     635: 'KEY_27B',
     636: 'KEY_27C',
     637: 'KEY_27D',
     638: 'KEY_27E',
     639: 'KEY_27F',
     640: 'KEY_280',
     641: 'KEY_281',
     642: 'KEY_282',
     643: 'KEY_283',
     644: 'KEY_284',
     645: 'KEY_285',
     646: 'KEY_286',
     647: 'KEY_287',
     648: 'KEY_288',
     649: 'KEY_289',
     650: 'KEY_28A',
     651: 'KEY_28B',
     652: 'KEY_28C',
     653: 'KEY_28D',
     654: 'KEY_28E',
     655: 'KEY_28F',
     656: 'KEY_MACRO1',
     657: 'KEY_MACRO2',
     658: 'KEY_MACRO3',
     659: 'KEY_MACRO4',
     660: 'KEY_MACRO5',
     661: 'KEY_MACRO6',
     662: 'KEY_MACRO7',
     663: 'KEY_MACRO8',
     664: 'KEY_MACRO9',
     665: 'KEY_MACRO10',
     666: 'KEY_MACRO11',
     667: 'KEY_MACRO12',
     668: 'KEY_MACRO13',
     669: 'KEY_MACRO14',
     670: 'KEY_MACRO15',
     671: 'KEY_MACRO16',
     672: 'KEY_MACRO17',
     673: 'KEY_MACRO18',
     674: 'KEY_MACRO19',
     675: 'KEY_MACRO20',
     676: 'KEY_MACRO21',
     677: 'KEY_MACRO22',
     678: 'KEY_MACRO23',
     679: 'KEY_MACRO24',
     680: 'KEY_MACRO25',
     681: 'KEY_MACRO26',
     682: 'KEY_MACRO27',
     683: 'KEY_MACRO28',
     684: 'KEY_MACRO29',
     685: 'KEY_MACRO30',
     686: 'KEY_2AE',
     687: 'KEY_2AF',
     688: 'KEY_MACRO_RECORD_START',
     689: 'KEY_MACRO_RECORD_STOP',
     690: 'KEY_MACRO_PRESET_CYCLE',
     691: 'KEY_MACRO_PRESET1',
     692: 'KEY_MACRO_PRESET2',
     693: 'KEY_MACRO_PRESET3',
     694: 'KEY_2B6',
     695: 'KEY_2B7',
     696: 'KEY_KBD_LCD_MENU1',
     697: 'KEY_KBD_LCD_MENU2',
     698: 'KEY_KBD_LCD_MENU3',
     699: 'KEY_KBD_LCD_MENU4',
     700: 'KEY_KBD_LCD_MENU5',
     701: 'KEY_2BD',
     702: 'KEY_2BE',
     703: 'KEY_2BF',
     704: 'BTN_TRIGGER_HAPPY1',
     705: 'BTN_TRIGGER_HAPPY2',
     706: 'BTN_TRIGGER_HAPPY3',
     707: 'BTN_TRIGGER_HAPPY4',
     708: 'BTN_TRIGGER_HAPPY5',
     709: 'BTN_TRIGGER_HAPPY6',
     710: 'BTN_TRIGGER_HAPPY7',
     711: 'BTN_TRIGGER_HAPPY8',
     712: 'BTN_TRIGGER_HAPPY9',
     713: 'BTN_TRIGGER_HAPPY10',
     714: 'BTN_TRIGGER_HAPPY11',
     715: 'BTN_TRIGGER_HAPPY12',
     716: 'BTN_TRIGGER_HAPPY13',
     717: 'BTN_TRIGGER_HAPPY14',
     718: 'BTN_TRIGGER_HAPPY15',
     719: 'BTN_TRIGGER_HAPPY16',
     720: 'BTN_TRIGGER_HAPPY17',
     721: 'BTN_TRIGGER_HAPPY18',
     722: 'BTN_TRIGGER_HAPPY19',
     723: 'BTN_TRIGGER_HAPPY20',
     724: 'BTN_TRIGGER_HAPPY21',
     725: 'BTN_TRIGGER_HAPPY22',
     726: 'BTN_TRIGGER_HAPPY23',
     727: 'BTN_TRIGGER_HAPPY24',
     728: 'BTN_TRIGGER_HAPPY25',
     729: 'BTN_TRIGGER_HAPPY26',
     730: 'BTN_TRIGGER_HAPPY27',
     731: 'BTN_TRIGGER_HAPPY28',
     732: 'BTN_TRIGGER_HAPPY29',
     733: 'BTN_TRIGGER_HAPPY30',
     734: 'BTN_TRIGGER_HAPPY31',
     735: 'BTN_TRIGGER_HAPPY32',
     736: 'BTN_TRIGGER_HAPPY33',
     737: 'BTN_TRIGGER_HAPPY34',
     738: 'BTN_TRIGGER_HAPPY35',
     739: 'BTN_TRIGGER_HAPPY36',
     740: 'BTN_TRIGGER_HAPPY37',
     741: 'BTN_TRIGGER_HAPPY38',
     742: 'BTN_TRIGGER_HAPPY39',
     743: 'BTN_TRIGGER_HAPPY40',
     744: 'KEY_2E8',
     745: 'KEY_2E9',
     746: 'KEY_2EA',
     747: 'KEY_2EB',
     748: 'KEY_2EC',
     749: 'KEY_2ED',
     750: 'KEY_2EE',
     751: 'KEY_2EF',
     752: 'KEY_2F0',
     753: 'KEY_2F1',
     754: 'KEY_2F2',
     755: 'KEY_2F3',
     756: 'KEY_2F4',
     757: 'KEY_2F5',
     758: 'KEY_2F6',
     759: 'KEY_2F7',
     760: 'KEY_2F8',
     761: 'KEY_2F9',
     762: 'KEY_2FA',
     763: 'KEY_2FB',
     764: 'KEY_2FC',
     765: 'KEY_2FD',
     766: 'KEY_2FE',
     767: 'KEY_MAX'},
 2: {0: 'REL_X',
     1: 'REL_Y',
     2: 'REL_Z',
     3: 'REL_RX',
     4: 'REL_RY',
     5: 'REL_RZ',
     6: 'REL_HWHEEL',
     7: 'REL_DIAL',
     8: 'REL_WHEEL',
     9: 'REL_MISC',
     10: 'REL_RESERVED',
     11: 'REL_WHEEL_HI_RES',
     12: 'REL_HWHEEL_HI_RES',
     13: 'REL_0D',
     14: 'REL_0E',
     15: 'REL_MAX'},
 3: {0: 'ABS_X',
     1: 'ABS_Y',
     2: 'ABS_Z',
     3: 'ABS_RX',
     4: 'ABS_RY',
     5: 'ABS_RZ',
     6: 'ABS_THROTTLE',
     7: 'ABS_RUDDER',
     8: 'ABS_WHEEL',
     9: 'ABS_GAS',
     10: 'ABS_BRAKE',
     11: 'ABS_0B',
     12: 'ABS_0C',
     13: 'ABS_0D',
     14: 'ABS_0E',
     15: 'ABS_0F',
     16: 'ABS_HAT0X',
     17: 'ABS_HAT0Y',
     18: 'ABS_HAT1X',
     19: 'ABS_HAT1Y',
     20: 'ABS_HAT2X',
     21: 'ABS_HAT2Y',
     22: 'ABS_HAT3X',
     23: 'ABS_HAT3Y',
     24: 'ABS_PRESSURE',
     25: 'ABS_DISTANCE',
     26: 'ABS_TILT_X',
     27: 'ABS_TILT_Y',
     28: 'ABS_TOOL_WIDTH',
     29: 'ABS_1D',
     30: 'ABS_1E',
     31: 'ABS_1F',
     32: 'ABS_VOLUME',
     33: 'ABS_21',
     34: 'ABS_22',
     35: 'ABS_23',
     36: 'ABS_24',
     37: 'ABS_25',
     38: 'ABS_26',
     39: 'ABS_27',
     40: 'ABS_MISC',
     41: 'ABS_29',
     42: 'ABS_2A',
     43: 'ABS_2B',
     44: 'ABS_2C',
     45: 'ABS_2D',
     46: 'ABS_RESERVED',
     47: 'ABS_MT_SLOT',
     48: 'ABS_MT_TOUCH_MAJOR',
     49: 'ABS_MT_TOUCH_MINOR',
     50: 'ABS_MT_WIDTH_MAJOR',
     51: 'ABS_MT_WIDTH_MINOR',
     52: 'ABS_MT_ORIENTATION',
     53: 'ABS_MT_POSITION_X',
     54: 'ABS_MT_POSITION_Y',
     55: 'ABS_MT_TOOL_TYPE',
     56: 'ABS_MT_BLOB_ID',
     57: 'ABS_MT_TRACKING_ID',
     58: 'ABS_MT_PRESSURE',
     59: 'ABS_MT_DISTANCE',
     60: 'ABS_MT_TOOL_X',
     61: 'ABS_MT_TOOL_Y',
     62: 'ABS_3E',
     63: 'ABS_MAX'},
 4: {0: 'MSC_SERIAL',
     1: 'MSC_PULSELED',
     2: 'MSC_GESTURE',
     3: 'MSC_RAW',
     4: 'MSC_SCAN',
     5: 'MSC_TIMESTAMP',
     6: 'MSC_06',
     7: 'MSC_MAX'},
 5: {0: 'SW_LID',
     1: 'SW_TABLET_MODE',
     2: 'SW_HEADPHONE_INSERT',
     3: 'SW_RFKILL_ALL',
     4: 'SW_MICROPHONE_INSERT',
     5: 'SW_DOCK',
     6: 'SW_LINEOUT_INSERT',
     7: 'SW_JACK_PHYSICAL_INSERT',
     8: 'SW_VIDEOOUT_INSERT',
     9: 'SW_CAMERA_LENS_COVER',
     10: 'SW_KEYPAD_SLIDE',
     11: 'SW_FRONT_PROXIMITY',
     12: 'SW_ROTATE_LOCK',
     13: 'SW_LINEIN_INSERT',
     14: 'SW_MUTE_DEVICE',
     15: 'SW_PEN_INSERTED',
     16: 'SW_MACHINE_COVER'},
 17: {0: 'LED_NUML',
      1: 'LED_CAPSL',
      2: 'LED_SCROLLL',
      3: 'LED_COMPOSE',
      4: 'LED_KANA',
      5: 'LED_SLEEP',
      6: 'LED_SUSPEND',
      7: 'LED_MUTE',
      8: 'LED_MISC',
      9: 'LED_MAIL',
      10: 'LED_CHARGING',
      11: 'LED_0B',
      12: 'LED_0C',
      13: 'LED_0D',
      14: 'LED_0E',
      15: 'LED_MAX'},
 18: {0: 'SND_CLICK',
      1: 'SND_BELL',
      2: 'SND_TONE',
      3: 'SND_03',
      4: 'SND_04',
      5: 'SND_05',
      6: 'SND_06',
      7: 'SND_MAX'},
 20: {0: 'REP_DELAY', 1: 'REP_PERIOD'},
 21: {0: 'FF_STATUS_STOPPED',
      1: 'FF_STATUS_MAX',
      2: 'FF_02',
      3: 'FF_03',
      4: 'FF_04',
      5: 'FF_05',
      6: 'FF_06',
      7: 'FF_07',
      8: 'FF_08',
      9: 'FF_09',
      10: 'FF_0A',
      11: 'FF_0B',
      12: 'FF_0C',
      13: 'FF_0D',
      14: 'FF_0E',
      15: 'FF_0F',
      16: 'FF_10',
      17: 'FF_11',
      18: 'FF_12',
      19: 'FF_13',
      20: 'FF_14',
      21: 'FF_15',
      22: 'FF_16',
      23: 'FF_17',
      24: 'FF_18',
      25: 'FF_19',
      26: 'FF_1A',
      27: 'FF_1B',
      28: 'FF_1C',
      29: 'FF_1D',
      30: 'FF_1E',
      31: 'FF_1F',
      32: 'FF_20',
      33: 'FF_21',
      34: 'FF_22',
      35: 'FF_23',
      36: 'FF_24',
      37: 'FF_25',
      38: 'FF_26',
      39: 'FF_27',
      40: 'FF_28',
      41: 'FF_29',
      42: 'FF_2A',
      43: 'FF_2B',
      44: 'FF_2C',
      45: 'FF_2D',
      46: 'FF_2E',
      47: 'FF_2F',
      48: 'FF_30',
      49: 'FF_31',
      50: 'FF_32',
      51: 'FF_33',
      52: 'FF_34',
      53: 'FF_35',
      54: 'FF_36',
      55: 'FF_37',
      56: 'FF_38',
      57: 'FF_39',
      58: 'FF_3A',
      59: 'FF_3B',
      60: 'FF_3C',
      61: 'FF_3D',
      62: 'FF_3E',
      63: 'FF_3F',
      64: 'FF_40',
      65: 'FF_41',
      66: 'FF_42',
      67: 'FF_43',
      68: 'FF_44',
      69: 'FF_45',
      70: 'FF_46',
      71: 'FF_47',
      72: 'FF_48',
      73: 'FF_49',
      74: 'FF_4A',
      75: 'FF_4B',
      76: 'FF_4C',
      77: 'FF_4D',
      78: 'FF_4E',
      79: 'FF_4F',
      80: 'FF_RUMBLE',
      81: 'FF_PERIODIC',
      82: 'FF_CONSTANT',
      83: 'FF_SPRING',
      84: 'FF_FRICTION',
      85: 'FF_DAMPER',
      86: 'FF_INERTIA',
      87: 'FF_RAMP',
      88: 'FF_SQUARE',
      89: 'FF_TRIANGLE',
      90: 'FF_SINE',
      91: 'FF_SAW_UP',
      92: 'FF_SAW_DOWN',
      93: 'FF_CUSTOM',
      94: 'FF_5E',
      95: 'FF_5F',
      96: 'FF_GAIN',
      97: 'FF_AUTOCENTER',
      98: 'FF_62',
      99: 'FF_63',
      100: 'FF_64',
      101: 'FF_65',
      102: 'FF_66',
      103: 'FF_67',
      104: 'FF_68',
      105: 'FF_69',
      106: 'FF_6A',
      107: 'FF_6B',
      108: 'FF_6C',
      109: 'FF_6D',
      110: 'FF_6E',
      111: 'FF_6F',
      112: 'FF_70',
      113: 'FF_71',
      114: 'FF_72',
      115: 'FF_73',
      116: 'FF_74',
      117: 'FF_75',
      118: 'FF_76',
      119: 'FF_77',
      120: 'FF_78',
      121: 'FF_79',
      122: 'FF_7A',
      123: 'FF_7B',
      124: 'FF_7C',
      125: 'FF_7D',
      126: 'FF_7E',
      127: 'FF_MAX'},
 22: {},
 23: {},
 31: {}}
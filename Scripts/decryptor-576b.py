
from itertools import cycle

BYTE_MAX_VALUE = 127

# egrep -e '    public static String |        byte\[\] bArr = |        byte\[\] bArr3 = '

encoded = {

    # sources/com/sponsor/economy/LUzOeBsTwTdRzFfQhTxGsEsRjZuIxJoDs.java

    'aboveriver' : [
        bytes([ 41, 33, 70, 48, 42, 85, 44, 42, 85, 44 ]),
        bytes([ 95, 78, 37 ])
    ],
    'artisttaste' : [
        bytes([ 105, 50, 49, 77, 59, 36, 125, 36 ]),
        bytes([ 14, 87, 69 ])
    ],
    'augustsleep' : [
        bytes([ 97, 86, 107, 119, 74, 109, 104, 72, 116, 102, 72, 116, 102, 68 ]),
        bytes([ 2, 46, 30 ])
    ],
    'balancetortoise' : [
        bytes([ 105, 10, 82, 8 ]),
        bytes([ 10, 82 ])
    ],
    'convincefunny' : [
        bytes([ 37, 81, 60, 72, 51, 84, 0, 118, 7, 72, 39, 84, 55 ]),
        bytes([ 68, 48 ])
    ],
    'cornpumpkin' : [
        bytes([ 91, 106, 81, 116 ]),
        bytes([ 52, 26 ])
    ],
    'creditblind' : [
        bytes([ 25, 62, 3, 31, 61 ]),
        bytes([ 45, 15, 50 ])
    ],
    'dentistchaos' : [
        bytes([ 36, 65, 60, 32, 79, 36, 59, 85, 61, 59, 81, 35, 20, 114, 2 ]),
        bytes([ 83, 54, 69 ])
    ],
    'dreamkangaroo' : [
        bytes([ 82, 56, 81, 46, 66, 14, 113, 14, 96, 61 ]),
        bytes([ 36, 91 ])
    ],
    'fabricscrub' : [
        bytes([ 73, 44, 69, 51, 79 ]),
        bytes([ 42, 64 ])
    ],
    'fewnut' : [
        bytes([ 124, 34, 111, 6, 104, 52, 126, 51, 104 ]),
        bytes([ 27, 71 ])
    ],
    'galaxyvast' : [
        bytes([ 99, 120, 111, 97, 115, 106, 115, 104, 100, 102, 104, 100, 102, 104 ]),
        bytes([ 0 ])
    ],
    'genuinemuch' : [
        bytes([ 74, 62, 83, 46, 88, 4, 101, 25, 111, 21, 120, 51, 82, 62, 68 ]),
        bytes([ 60, 93 ])
    ],
    'goatcitizen' : [
        bytes([ 84, 34, 71, 35 ]),
        bytes([ 38, 71 ])
    ],
    'lifthover' : [
        bytes([ 54, 97, 104, 38, 104 ]),
        bytes([ 85, 13, 7 ])
    ],
    'mountainginger' : [
        bytes([ 88, 90, 75, 124, 83, 94, 76, 76 ]),
        bytes([ 63 ])
    ],
    'needgreen' : [
        bytes([ 39, 106, 52, 76, 44, 110, 51, 124 ]),
        bytes([ 64, 15 ])
    ],
    'nosecoast' : [
        bytes([ 74, 84, 65, 74, 74, 68, 74, 70, 70, 81, 70, 81 ]),
        bytes([ 34 ])
    ],
    'pagejeans' : [
        bytes([ 35, 63, 38, 62, 49, 115, 33, 54, 32, 48, 38, 54 ]),
        bytes([ 83 ])
    ],
    'polesplit' : [
        bytes([ 55, 84, 36, 115, 41, 69, 53, 66 ]),
        bytes([ 80, 49 ])
    ],
    'profitera' : [
        bytes([ 61, 36, 35, 34, 47 ]),
        bytes([ 74, 86 ])
    ],
    'railinitial' : [
        bytes([ 87, 110, 105, 119, 121, 126, 83, 126, 93, 87, 126, 101 ]),
        bytes([ 54, 10, 13 ])
    ],
    'reducegiggle' : [
        bytes([ 42, 40, 57, 14, 33, 44, 62, 62 ]),
        bytes([ 77 ])
    ],
    'richarena' : [
        bytes([ 121, 123, 106, 93, 114, BYTE_MAX_VALUE, 109, 109 ]),
        bytes([ 30 ])
    ],
    'saucemesh' : [
        bytes([ 49, 46, 58, 45, 46, 61, 50, 38, 50, 58, 45, 47, 47 ]),
        bytes([ 94 ])
    ],
    'sightselect' : [
        bytes([ 62, 41, 45, 40 ]),
        bytes([ 76 ])
    ],
    'snowalert' : [
        bytes([ 56, 46, 45, 46, 63, 40, 51, 63, 51, 63, 61, 51, 63, 61, 51 ]),
        bytes([ 91 ])
    ],
    'sufferseat' : [
        bytes([ 3, 43, 47, 19, 34 ]),
        bytes([ 96, 71, 64 ])
    ],
    'tonedrip' : [
        bytes([ 87, 38, 54, 71, 38, 47, 75, 42, 47, 75, 42, 47, 75, 42, 47, 75, 42, 47 ]),
        bytes([ 33, 64, 69 ])
    ],
    'toothnear' : [
        bytes([ 8, 104, 90, 62, 114, 86, 33, 108, 68, 33, 111 ]),
        bytes([ 70, 11, 50 ])
    ],
    'trashflight' : [
        bytes([ 49, 45, 55, 61, 55, 42, 43, 61, 35, 34, 52, 42, 43 ]),
        bytes([ 71, 78 ])
    ],
    'vastarrange' : [
        bytes([ 73, 36, 90, 2, 66, 32, 93, 50 ]),
        bytes([ 46, 65 ])
    ],
    'venturesleep' : [
        bytes([ 6, 99, 22, 113, 16, 119, 1, 99, 17, 97, 52, 70, 20 ]),
        bytes([ 98, 5 ])
    ],
    'voidfossil' : [
        bytes([ 121, 14, 115, 74, 24, 114, 74, 24, 117, 74, 59, 80 ]),
        bytes([ 15, 93, 54 ])
    ],
    'walksaddle' : [
        bytes([ 86, 56, 115, 82, 50, 120, 76, 48, BYTE_MAX_VALUE, 82, 4, 73, 112 ]),
        bytes([ 52, 86, 27 ]),
    ],

    # sources/com/sponsor/economy/OFaTiNcSoBnDbPyUmFiRuDuKf.java

    'brothervalve' : [
        bytes([ 122, 120, 105 ]),
        bytes([ 29 ])
    ],
    'cashsystem' : [
        bytes([ 2, 114, 7, 110, 12, 117, 7, 50, 2, 108, 19, 50, 47, 115, 2, 120, 6, 120, 34, 108, 8 ]),
        bytes([ 99, 28 ])
    ],
    'cigarurge' : [
        bytes([ 56, 126, 51, 105, 37, 44, 63, 101, 36, 120, 56, 126, 46, 44, 59, 121, 52, 103, 46 ]),
        bytes([ 87, 12 ])
    ],
    'dadmind' : [
        bytes([ 102, 89, 62, 66, 80, 43, 114, 79 ]),
        bytes([ 1, 60, 74 ])
    ],
    'damparrow' : [
        bytes([ 79, 73, 107 ]),
        bytes([ 40, 44, 31 ])
    ],
    'dynamicauthor' : [
        bytes([ 43, 61, 58, 58, 45, 38, 60, 9, 43, 60, 33, 62, 33, 60, 49, 28, 32, 58, 45, 41, 44 ]),
        bytes([ 72 ])
    ],
    'endorsemarble' : [
        bytes([ 59, 57, 40 ]),
        bytes([ 92 ])
    ],
    'enhancelawn' : [
        bytes([ 100, 74, 101, 104, 122, 122, 69, 102, 104, 109, 108, 123 ]),
        bytes([ 9 ])
    ],
    'leftbuild' : [
        bytes([ 94, 79, 94, 79, 94, 90, 92, 77, 92, 78, 92, 78, 92, 78 ]),
        bytes([ 58, 41 ])
    ],
    'paymentslam' : [
        bytes([ 59, 110, 35 ]),
        bytes([ 92, 11, 87 ])
    ],
    'surprisehand' : [
        bytes([ 99, 117, 102, 105, 109, 114, 102, 53, 99, 107, 114, 53, 67, 120, 118, 114, 116, 114, 118, 98, 86, 115, 112, 126, 99, BYTE_MAX_VALUE ]),
        bytes([ 2, 27 ])
    ],
    'tonguehub' : [
        bytes([ 105, 65, 101, 114, 111, 112, 99, 116, 119 ]),
        bytes([ 4, 17 ])
    ],
    'wetprint' : [
        bytes([ 102, 124, 124, 118, 109, 97, 109, 115, 110, 115, 110, 102, 110, 110, 110, 99, 99, 97 ]),
        bytes([ 5 ])
    ],

    # sources/com/sponsor/economy/IIwZlGwOsUhRkOnNyNkUc.java

    'blossomcollect' : [
        bytes([ 59, 63, 116, 38, 49, 36, 56, 53, 55, 49, 116, 39, 32, 38, 61, 58, 51, 116, 54, 61, 32, 55, 60 ]),
        bytes([ 84 ])
    ],
    'burgerjar' : [
        bytes([ 88, 80, 94, 91, 80, 24, 79, 80, 94, 24, 86, 89, 82, 86, 27, 89, 82, 85 ]),
        bytes([ 59, 56 ])
    ],
    'catalogclient' : [
        bytes([ 47, 32, 42, 60, 33, 39, 42, 96, 47, 62, 62, 96, 13, 33, 32, 58, 43, 54, 58, 7, 35, 62, 34 ]),
        bytes([ 78 ])
    ],
    'clickjudge' : [
        bytes([ 47, 49, 117, 17, 9, 86, 106, 10, 82, 43, 14 ]),
        bytes([ 68, 96, 33 ])
    ],
    'demisesimple' : [
        bytes([ 85, 94, 112, 112, 74, 119, 114, 107, 119, 115 ]),
        bytes([ 17, 39, 30 ])
    ],
    'equipspy' : [
        bytes([ 101, 88, 79, 64, 76, 72, 66, 110, 81, 85, 101, 68, 89 ]),
        bytes([ 33 ])
    ],
    'exoticfog' : [
        bytes([ 86, 68, 50, 69, 69, 63, 83, 4, 55, 71, 90, 120, 123, 69, 55, 83, 79, 50, 118, 90, 61 ]),
        bytes([ 55, 42, 86 ])
    ],
    'glowpalm' : [
        bytes([ 100, 109, 100, 119, 96, 117, 104, 110, 111, 33, 96, 98, 117, 110, 115, 33, 117, 96, 111, 106 ]),
        bytes([ 1 ])
    ],
    'indexrelax' : [
        bytes([ 77, 7, 85, 60, 69, 58, 99, 39, 78, 60, 69, 48, 84 ]),
        bytes([ 32, 72 ])
    ],
    'inspirefind' : [
        bytes([ 53, 58, 89, 53, 45, 69 ]),
        bytes([ 84, 78, 45 ])
    ],
    'ivoryvanish' : [
        bytes([ 39, 68, 54, 83, 115, 94, 50, 69, 59, 22, 38, 70 ]),
        bytes([ 83, 54 ])
    ],
    'leveljourney' : [
        bytes([ 115, 95, 125, 106, 119, 104, 119, 106, 103, 74, 118, 108, 123, BYTE_MAX_VALUE, 122 ]),
        bytes([ 30 ])
    ],
    'pillrice' : [
        bytes([ 62, 26, 61, 58, 39, 58, 50, 63, 18, 35, 35, 63, 58, 48, 50, 39, 58, 60, 61 ]),
        bytes([ 83 ])
    ],
    'proofprogram' : [
        bytes([ 93, 81, 83, 16, 77, 90, 85, 74, 81, 81, 82, 77, 16, 95, 80, 90, 76, 81, 87, 90, 16, BYTE_MAX_VALUE, 78, 78 ]),
        bytes([ 62 ])
    ],
    'ranchrather' : [
        bytes([ 54, 47, 42, 41, 60, 123, 55, 62, 53, 62, 36, 47, 54 ]),
        bytes([ 69, 91 ])
    ],
    'riflesteel' : [
        bytes([ 35, 15, 62, 62, 34, 39, 45, 47, 58, 39, 33, 32 ]),
        bytes([ 78 ])
    ],
    'seedday' : [
        bytes([ 116, 88, 117, 117, 88, 105, 105, 117, 112, 122, 120, 109, 112, 118, 119, 106 ]),
        bytes([ 25 ])
    ],
    'tapesix' : [
        bytes([ 62, 49, 59, 45, 48, 54, 59, 113, 62, 47, 47, 113, 30, 60, 43, 54, 41, 54, 43, 38, 11, 55, 45, 58, 62, 59 ]),
        bytes([ 95 ])
    ],
    'wordwet' : [
        bytes([ 124, 20, 112, 39, 122, 37, 118, 33, 88, 42, 119, 43 ]),
        bytes([ 17, 68 ])
    ]

}


for n, e in encoded.items():

    s = e[0]
    k = e[1]

    d = bytes([ x ^ y for x, y in zip(s, cycle(k))])

    print('%s(): %s' % (n, d.decode('utf8')))

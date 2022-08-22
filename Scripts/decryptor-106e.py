
from itertools import cycle

BYTE_MAX_VALUE = 127

# egrep -e '    public static String |        byte\[\] bArr = |        byte\[\] bArr3 = '

encoded = {

    # sources/com/cabin/p000float/DLtWoUoAcFlFgHhSxYxLcFmIxAzCpOeBbEsJeHjBoIa.java

    'casualsign' : [
        bytes([ 102, 91, 76, 67, 79, 75, 65, 109, 82, 86, 102, 71, 90 ]),
        bytes([ 34 ])
    ],
    'claimenvelope' : [
        bytes([ 102, 43, 126, 117, 42, 115, 99, 107, 123, 119, 53, 52, 68, 42, 116, 115, 32, 98, 115, 12, 119, 119, 41 ]),
        bytes([ 7, 69, 26 ])
    ],
    'crackroom' : [
        bytes([ 115, 58, 91, 98, 104, 86, 102, 59, 86, 39, 61, 78 ]),
        bytes([ 7, 72, 62 ])
    ],
    'dependawake' : [
        bytes([ 115, 23, 114, 58, 95, 38, 110, 58, 119, 53, BYTE_MAX_VALUE, 34, 119, 57, 112, 37 ]),
        bytes([ 30, 86 ])
    ],
    'detailenable' : [
        bytes([ 121, 108, 108, 121, 123, 112 ]),
        bytes([ 24 ])
    ],
    'elevatorkite' : [
        bytes([ 100, 72, 121, 121, 101, 96, 106, 104, 125, 96, 102, 103 ]),
        bytes([ 9 ])
    ],
    'gingerfade' : [
        bytes([ 58, 76, 34, 119, 50, 113, 20, 108, 57, 119, 50, 123, 35 ]),
        bytes([ 87, 3 ])
    ],
    'hirefine' : [
        bytes([ 100, 96, 43, 121, 110, 123, 103, 106, 104, 110, 43, 120, BYTE_MAX_VALUE, 121, 98, 101, 108, 43, 105, 98, BYTE_MAX_VALUE, 104, 99 ]),
        bytes([ 11 ])
    ],
    'hoversing' : [
        bytes([ 124, 114, 81, 120, 79, 86, 112, 87, 126, 97, 75, 83, 120, 88, 94, 101, 82, 80, BYTE_MAX_VALUE ]),
        bytes([ 17, 59, 63 ])
    ],
    'immensebetray' : [
        bytes([ 109, 119, 99, 66, 105, 64, 105, 66, 121, 98, 104, 68, 101, 87, 100 ]),
        bytes([ 0, 54 ])
    ],
    'leisurewet' : [
        bytes([ BYTE_MAX_VALUE, 112, 119, 118, 23, 83, 74, 86, 87 ]),
        bytes([ 57 ])
    ],
    'natureyouth' : [
        bytes([ 57, BYTE_MAX_VALUE, 57, 101, 61, 103, 53, 124, 50, 51, 61, 112, 40, 124, 46, 51, 40, 114, 50, 120 ]),
        bytes([ 92, 19 ])
    ],
    'obscurebuzz' : [
        bytes([ 95, 104, 83, 91, 89, 89, 85, 93, 123, 86, 84, 87 ]),
        bytes([ 50, 56 ])
    ],
    'omitcolumn' : [
        bytes([ 0, 115, 80, 19, 114, 93, 5, 51, 85, 17, 109, 26, 32, 126, 64, 8, 107, 93, 21, 100, 96, 9, 111, 81, 0, 121 ]),
        bytes([ 97, 29, 52 ])
    ],
    'peanutugly' : [
        bytes([ 55, 33, 49, 42, 63, 105, 32, 33, 49, 105, 57, 40, 61, 39, 116, 40, 61, 36 ]),
        bytes([ 84, 73 ])
    ],
    'proofspirit' : [
        bytes([ 32, 45, 107, 109, 49, 98, 40, 54, 105, 44, 46, 117, 109, 35, 104, 39, 48, 105, 42, 38, 40, 2, 50, 118 ]),
        bytes([ 67, 66, 6 ])
    ],
    'saddleunfair' : [
        bytes([ 90, 93, 70, 91, 80, 9, 91, 76, 89, 76, 72, 93, 90 ]),
        bytes([ 41 ])
    ],
    'successpattern' : [
        bytes([ 72, 76, 77, 80, 70, 75, 77, 12, 72, 82, 89, 12, 101, 77, 72, 70, 76, 70, 104, 82, 66 ]),
        bytes([ 41, 34 ])
    ],
    'thingmisery' : [
        bytes([ 73, 116, 99, 108, 96, 100, 110, 65, 100, 111 ]),
        bytes([ 13 ])
    ],

    # sources/com/cabin/p000float/CYtFbPhWuRaQbIyZuJx.java

    'alarmconfirm' : [
        bytes([ 38, 56, 45, 38, 38, 40, 38, 42, 42, 61, 42, 61 ]),
        bytes([ 78 ])
    ],
    'assaulttongue' : [
        bytes([ 74, 95, 83, 79, 88, 101, 101, 120, 111, 116, 120, 82, 82, 95, 68 ]),
        bytes([ 60 ])
    ],
    'cannonsample' : [
        bytes([ 66, 93, 72, 67 ]),
        bytes([ 45 ])
    ],
    'chaptercanoe' : [
        bytes([ 48, 47, 72, 51, 56 ]),
        bytes([ 71, 93, 33 ])
    ],
    'crewrace' : [
        bytes([ 93, 65, 88, 64, 79, 13, 95, 72, 94, 78, 88, 72 ]),
        bytes([ 45 ])
    ],
    'firstprotect' : [
        bytes([ 81, 37, 82, 71 ]),
        bytes([ 35, 64, 51 ])
    ],
    'flagtoddler' : [
        bytes([ 54, 35, 48, 51, 48, 36, 44, 51, 36, 44, 51, 36, 44 ]),
        bytes([ 64 ])
    ],
    'flightblanket' : [
        bytes([ 113, 106, 103, 103, 118, 97, 120, 116, 120, 118, 116, 120, 118, 120 ]),
        bytes([ 18 ])
    ],
    'gossipbuild' : [
        bytes([ 82, 80, 65, 118, 89, 84, 70, 70 ]),
        bytes([ 53 ])
    ],
    'griefpolice' : [
        bytes([ 73, BYTE_MAX_VALUE, 121, 89, 118 ]),
        bytes([ 42, 19, 22 ])
    ],
    'hipsecurity' : [
        bytes([ 53, 57, 63, 49, 51, 52, 47, 49, 51, 49, 5, 5, 19 ]),
        bytes([ 87 ])
    ],
    'humorcrouch' : [
        bytes([ 35, 60, 40, 63, 60, 47, 32, 52, 32, 40, 63, 61, 61 ]),
        bytes([ 76 ])
    ],
    'jeansdonkey' : [
        bytes([ 55, 126, 36, 88, 60, 122, 35, 104 ]),
        bytes([ 80, 27 ])
    ],
    'juicemanage' : [
        bytes([ 76, 100, 47, 72, 106, 55, 83, 112, 46, 83, 116, 48, 124, 87, 17 ]),
        bytes([ 59, 19, 86 ])
    ],
    'magnetsatisfy' : [
        bytes([ 65, 96, 58, 101, 105, 47, 85, 118 ]),
        bytes([ 38, 5, 78 ])
    ],
    'meritnote' : [
        bytes([ 114, 98, 48, 107, 105, 35, 119, 105, 35, 119 ]),
        bytes([ 4, 13, 83 ])
    ],
    'optionjealous' : [
        bytes([ 64, 42, 66, 80, 42, 91, 92, 38, 91, 92, 38, 91, 92, 38, 91, 92, 38, 91 ]),
        bytes([ 54, 76, 49 ])
    ],
    'pluckillness' : [
        bytes([ 73, 32, 106, 27, 75, 38 ]),
        bytes([ 57, 67 ])
    ],
    'rapidvelvet' : [
        bytes([ 104, 46, 120, 60, 126, 58, 111, 46, BYTE_MAX_VALUE, 44, 90, 11, 122 ]),
        bytes([ 12, 72 ])
    ],
    'rigidcable' : [
        bytes([ 63, 39, 88, 61, 44, 93, 47, 55, 83, 58, 55, 83, 58, 55 ]),
        bytes([ 92, 95, 55 ])
    ],
    'saltthank' : [
        bytes([ 45, 45, 52, 52, 59, 40, 8, 10, 15, 52, 47, 40, 63 ]),
        bytes([ 76 ])
    ],
    'seekmake' : [
        bytes([ 49, 77, 41, 33, 68 ]),
        bytes([ 82, 33, 70 ])
    ],
    'shrugcheese' : [
        bytes([ 104, 52, 88, 107, 49, 120, 75, 2, 105, 120 ]),
        bytes([ 30, 87, 45 ])
    ],
    'snakenerve' : [
        bytes([ 120, 97, 107, 71, 115, 101, 108, 119 ]),
        bytes([ 31, 4 ])
    ],
    'syrupmeat' : [
        bytes([ 86, 84, 69, 114, 93, 80, 66, 66 ]),
        bytes([ 49 ])
    ],
    'tennispromote' : [
        bytes([ 56, 109, 11, 123, 11, 122, 11, 123, 13, 123, 40, 88 ]),
        bytes([ 78, 62 ])
    ],
    'titlebulb' : [
        bytes([ 107, 65, 120, 101, BYTE_MAX_VALUE, 87, 105, 80, BYTE_MAX_VALUE ]),
        bytes([ 12, 36 ])
    ],
    'toyvote' : [
        bytes([ 110, 77, 47, 74, 68, 58, 122, 91 ]),
        bytes([ 9, 40, 91 ])
    ],
    'trustorgan' : [
        bytes([ 51, 49, 32, 22, 45, 32, 49, 39 ]),
        bytes([ 84 ])
    ],
    'tuitionhour' : [
        bytes([ 85, 126, 64, 126, 82, 120, 94, 111, 94, 111, 80, 99, 82, 109, 94 ]),
        bytes([ 54, 11 ])
    ],
    'umbrellacolor' : [
        bytes([ 41, 120, 58, 121 ]),
        bytes([ 91, 29 ])
    ],
    'variousorbit' : [
        bytes([ 111, 96, 99, BYTE_MAX_VALUE, 105 ]),
        bytes([ 12 ])
    ],
    'wantchalk' : [
        bytes([ 80, 32, 85, 5, 66, 55, 84, 48, 97, 37, 69, 44 ]),
        bytes([ 49, 68 ])
    ],
    'whispercasual' : [
        bytes([ 105, 99, 72, 95, 121, 68, 64, 103, 86, 64, 100 ]),
        bytes([ 39, 0, 32 ])
    ],
    'wisejewel' : [
        bytes([ 40, 45, 45, 46, 46 ]),
        bytes([ 28 ]),
    ],

    # ./sources/com/cabin/p000float/TJcYuNuLzDdTbCtLzHxFzIdEpMtRlDxBmCiOuFrZxPaYsLzRk.java

    'abusejunior' : [
        bytes([ 59, 56, 59, 56, 59, 45, 57, 58, 57, 57, 57, 57, 57, 57 ]),
        bytes([ 95, 94 ])
    ],
    'alcoholfestival' : [
        bytes([ 4, 6, 23 ]),
        bytes([ 99 ])
    ],
    'crushspirit' : [
        bytes([ 125, 103, 103, 109, 118, 122, 118, 104, 117, 104, 117, 125, 117, 117, 117, 120, 120, 122 ]),
        bytes([ 30 ])
    ],
    'drawleopard' : [
        bytes([ 122, 108, 107, 107, 124, 119, 109, 88, 122, 109, 112, 111, 112, 109, 96, 77, 113, 107, 124, 120, 125 ]),
        bytes([ 25 ])
    ],
    'earthmaster' : [
        bytes([ 6, 111, 81 ]),
        bytes([ 97, 10, 37 ])
    ],
    'eraseopen' : [
        bytes([ 44, 86, 68, 32, 102, 91, 13, 122, 73, 37, 112, 90 ]),
        bytes([ 65, 21, 40 ])
    ],
    'flykingdom' : [
        bytes([ 43, 67, 87, 56, 66, 90, 46, 3, 82, 58, 93, 29, 11, 78, 71, 35, 91, 90, 62, 84, 103, 34, 95, 86, 43, 73 ]),
        bytes([ 74, 45, 51 ])
    ],
    'mandatetone' : [
        bytes([ 104, 77, 69, 102, 118, 69, 98, 120, 87 ]),
        bytes([ 5, 29, 36 ])
    ],
    'overdecide' : [
        bytes([ 66, 64, 81 ]),
        bytes([ 37 ])
    ],
    'seasonalley' : [
        bytes([ 42, 37, 47, 57, 36, 34, 47, 101, 42, 59, 59, 101, 7, 36, 42, 47, 46, 47, 10, 59, 32 ]),
        bytes([ 75 ])
    ],
    'shippoint' : [
        bytes([ 99, 112, 86, 105, 112, 18, 100, 107, 65, 120, 109, 64, 117, 34, 94, 121, 97, 89, 117 ]),
        bytes([ 12, 2, 50 ])
    ],
    'socialexcess' : [
        bytes([ 68, 77, 60, 96, 68, 41, 80, 91 ]),
        bytes([ 35, 40, 72 ])
    ],
    'stamppermit' : [
        bytes([ 80, 82, 67 ]),
        bytes([ 55 ])
    ],

}


for n, e in encoded.items():

    s = e[0]
    k = e[1]

    d = bytes([ x ^ y for x, y in zip(s, cycle(k))])

    print('%s(): %s' % (n, d.decode('utf8')))

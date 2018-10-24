import math
nums_dict = [(519432,525806),
(632382,518061),
(78864,613712),
(466580,530130),
(780495,510032),
(525895,525320),
(15991,714883),
(960290,502358),
(760018,511029),
(166800,575487),
(210884,564478),
(555151,523163),
(681146,515199),
(563395,522587),
(738250,512126),
(923525,503780),
(595148,520429),
(177108,572629),
(750923,511482),
(440902,532446),
(881418,505504),
(422489,534197),
(979858,501616),
(685893,514935),
(747477,511661),
(167214,575367),
(234140,559696),
(940238,503122),
(728969,512609),
(232083,560102),
(900971,504694),
(688801,514772),
(189664,569402),
(891022,505104),
(445689,531996),
(119570,591871),
(821453,508118),
(371084,539600),
(911745,504251),
(623655,518600),
(144361,582486),
(352442,541775),
(420726,534367),
(295298,549387),
(6530,787777),
(468397,529976),
(672336,515696),
(431861,533289),
(84228,610150),
(805376,508857),
(444409,532117),
(33833,663511),
(381850,538396),
(402931,536157),
(92901,604930),
(304825,548004),
(731917,512452),
(753734,511344),
(51894,637373),
(151578,580103),
(295075,549421),
(303590,548183),
(333594,544123),
(683952,515042),
(60090,628880),
(951420,502692),
(28335,674991),
(714940,513349),
(343858,542826),
(549279,523586),
(804571,508887),
(260653,554881),
(291399,549966),
(402342,536213),
(408889,535550),
(40328,652524),
(375856,539061),
(768907,510590),
(165993,575715),
(976327,501755),
(898500,504795),
(360404,540830),
(478714,529095),
(694144,514472),
(488726,528258),
(841380,507226),
(328012,544839),
(22389,690868),
(604053,519852),
(329514,544641),
(772965,510390),
(492798,527927),
(30125,670983),
(895603,504906),
(450785,531539),
(840237,507276),
(380711,538522),
(63577,625673),
(76801,615157),
(502694,527123),
(597706,520257),
(310484,547206),
(944468,502959),
(121283,591152),
(451131,531507),
(566499,522367),
(425373,533918),
(40240,652665),
(39130,654392),
(714926,513355),
(469219,529903),
(806929,508783),
(287970,550487),
(92189,605332),
(103841,599094),
(671839,515725),
(452048,531421),
(987837,501323),
(935192,503321),
(88585,607450),
(613883,519216),
(144551,582413),
(647359,517155),
(213902,563816),
(184120,570789),
(258126,555322),
(502546,527130),
(407655,535678),
(401528,536306),
(477490,529193),
(841085,507237),
(732831,512408),
(833000,507595),
(904694,504542),
(581435,521348),
(455545,531110),
(873558,505829),
(94916,603796),
(720176,513068),
(545034,523891),
(246348,557409),
(556452,523079),
(832015,507634),
(173663,573564),
(502634,527125),
(250732,556611),
(569786,522139),
(216919,563178),
(521815,525623),
(92304,605270),
(164446,576167),
(753413,511364),
(11410,740712),
(448845,531712),
(925072,503725),
(564888,522477),
(7062,780812),
(641155,517535),
(738878,512100),
(636204,517828),
(372540,539436),
(443162,532237),
(571192,522042),
(655350,516680),
(299741,548735),
(581914,521307),
(965471,502156),
(513441,526277),
(808682,508700),
(237589,559034),
(543300,524025),
(804712,508889),
(247511,557192),
(543486,524008),
(504383,526992),
(326529,545039),
(792493,509458),
(86033,609017),
(126554,589005),
(579379,521481),
(948026,502823),
(404777,535969),
(265767,554022),
(266876,553840),
(46631,643714),
(492397,527958),
(856106,506581),
(795757,509305),
(748946,511584),
(294694,549480),
(409781,535463),
(775887,510253),
(543747,523991),
(210592,564536),
(517119,525990),
(520253,525751),
(247926,557124),
(592141,520626),
(346580,542492),
(544969,523902),
(506501,526817),
(244520,557738),
(144745,582349),
(69274,620858),
(292620,549784),
(926027,503687),
(736320,512225),
(515528,526113),
(407549,535688),
(848089,506927),
(24141,685711),
(9224,757964),
(980684,501586),
(175259,573121),
(489160,528216),
(878970,505604),
(969546,502002),
(525207,525365),
(690461,514675),
(156510,578551),
(659778,516426),
(468739,529945),
(765252,510770),
(76703,615230),
(165151,575959),
(29779,671736),
(928865,503569),
(577538,521605),
(927555,503618),
(185377,570477),
(974756,501809),
(800130,509093),
(217016,563153),
(365709,540216),
(774508,510320),
(588716,520851),
(631673,518104),
(954076,502590),
(777828,510161),
(990659,501222),
(597799,520254),
(786905,509727),
(512547,526348),
(756449,511212),
(869787,505988),
(653747,516779),
(84623,609900),
(839698,507295),
(30159,670909),
(797275,509234),
(678136,515373),
(897144,504851),
(989554,501263),
(413292,535106),
(55297,633667),
(788650,509637),
(486748,528417),
(150724,580377),
(56434,632490),
(77207,614869),
(588631,520859),
(611619,519367),
(100006,601055),
(528924,525093),
(190225,569257),
(851155,506789),
(682593,515114),
(613043,519275),
(514673,526183),
(877634,505655),
(878905,505602),
(1926,914951),
(613245,519259),
(152481,579816),
(841774,507203),
(71060,619442),
(865335,506175),
(90244,606469),
(302156,548388),
(399059,536557),
(478465,529113),
(558601,522925),
(69132,620966),
(267663,553700),
(988276,501310),
(378354,538787),
(529909,525014),
(161733,576968),
(758541,511109),
(823425,508024),
(149821,580667),
(269258,553438),
(481152,528891),
(120871,591322),
(972322,501901),
(981350,501567),
(676129,515483),
(950860,502717),
(119000,592114),
(392252,537272),
(191618,568919),
(946699,502874),
(289555,550247),
(799322,509139),
(703886,513942),
(194812,568143),
(261823,554685),
(203052,566221),
(217330,563093),
(734748,512313),
(391759,537328),
(807052,508777),
(564467,522510),
(59186,629748),
(113447,594545),
(518063,525916),
(905944,504492),
(613922,519213),
(439093,532607),
(445946,531981),
(230530,560399),
(297887,549007),
(459029,530797),
(403692,536075),
(855118,506616),
(963127,502245),
(841711,507208),
(407411,535699),
(924729,503735),
(914823,504132),
(333725,544101),
(176345,572832),
(912507,504225),
(411273,535308),
(259774,555036),
(632853,518038),
(119723,591801),
(163902,576321),
(22691,689944),
(402427,536212),
(175769,572988),
(837260,507402),
(603432,519893),
(313679,546767),
(538165,524394),
(549026,523608),
(61083,627945),
(898345,504798),
(992556,501153),
(369999,539727),
(32847,665404),
(891292,505088),
(152715,579732),
(824104,507997),
(234057,559711),
(730507,512532),
(960529,502340),
(388395,537687),
(958170,502437),
(57105,631806),
(186025,570311),
(993043,501133),
(576770,521664),
(215319,563513),
(927342,503628),
(521353,525666),
(39563,653705),
(752516,511408),
(110755,595770),
(309749,547305),
(374379,539224),
(919184,503952),
(990652,501226),
(647780,517135),
(187177,570017),
(168938,574877),
(649558,517023),
(278126,552016),
(162039,576868),
(658512,516499),
(498115,527486),
(896583,504868),
(561170,522740),
(747772,511647),
(775093,510294),
(652081,516882),
(724905,512824),
(499707,527365),
(47388,642755),
(646668,517204),
(571700,522007),
(180430,571747),
(710015,513617),
(435522,532941),
(98137,602041),
(759176,511070),
(486124,528467),
(526942,525236),
(878921,505604),
(408313,535602),
(926980,503640),
(882353,505459),
(566887,522345),
(3326,853312),
(911981,504248),
(416309,534800),
(392991,537199),
(622829,518651),
(148647,581055),
(496483,527624),
(666314,516044),
(48562,641293),
(672618,515684),
(443676,532187),
(274065,552661),
(265386,554079),
(347668,542358),
(31816,667448),
(181575,571446),
(961289,502320),
(365689,540214),
(987950,501317),
(932299,503440),
(27388,677243),
(746701,511701),
(492258,527969),
(147823,581323),
(57918,630985),
(838849,507333),
(678038,515375),
(27852,676130),
(850241,506828),
(818403,508253),
(131717,587014),
(850216,506834),
(904848,504529),
(189758,569380),
(392845,537217),
(470876,529761),
(925353,503711),
(285431,550877),
(454098,531234),
(823910,508003),
(318493,546112),
(766067,510730),
(261277,554775),
(421530,534289),
(694130,514478),
(120439,591498),
(213308,563949),
(854063,506662),
(365255,540263),
(165437,575872),
(662240,516281),
(289970,550181),
(847977,506933),
(546083,523816),
(413252,535113),
(975829,501767),
(361540,540701),
(235522,559435),
(224643,561577),
(736350,512229),
(328303,544808),
(35022,661330),
(307838,547578),
(474366,529458),
(873755,505819),
(73978,617220),
(827387,507845),
(670830,515791),
(326511,545034),
(309909,547285),
(400970,536363),
(884827,505352),
(718307,513175),
(28462,674699),
(599384,520150),
(253565,556111),
(284009,551093),
(343403,542876),
(446557,531921),
(992372,501160),
(961601,502308),
(696629,514342),
(919537,503945),
(894709,504944),
(892201,505051),
(358160,541097),
(448503,531745),
(832156,507636),
(920045,503924),
(926137,503675),
(416754,534757),
(254422,555966),
(92498,605151),
(826833,507873),
(660716,516371),
(689335,514746),
(160045,577467),
(814642,508425),
(969939,501993),
(242856,558047),
(76302,615517),
(472083,529653),
(587101,520964),
(99066,601543),
(498005,527503),
(709800,513624),
(708000,513716),
(20171,698134),
(285020,550936),
(266564,553891),
(981563,501557),
(846502,506991),
(334,1190800),
(209268,564829),
(9844,752610),
(996519,501007),
(410059,535426),
(432931,533188),
(848012,506929),
(966803,502110),
(983434,501486),
(160700,577267),
(504374,526989),
(832061,507640),
(392825,537214),
(443842,532165),
(440352,532492),
(745125,511776),
(13718,726392),
(661753,516312),
(70500,619875),
(436952,532814),
(424724,533973),
(21954,692224),
(262490,554567),
(716622,513264),
(907584,504425),
(60086,628882),
(837123,507412),
(971345,501940),
(947162,502855),
(139920,584021),
(68330,621624),
(666452,516038),
(731446,512481),
(953350,502619),
(183157,571042),
(845400,507045),
(651548,516910),
(20399,697344),
(861779,506331),
(629771,518229),
(801706,509026),
(189207,569512),
(737501,512168),
(719272,513115),
(479285,529045),
(136046,585401),
(896746,504860),
(891735,505067),
(684771,514999),
(865309,506184),
(379066,538702),
(503117,527090),
(621780,518717),
(209518,564775),
(677135,515423),
(987500,501340),
(197049,567613),
(329315,544673),
(236756,559196),
(357092,541226),
(520440,525733),
(213471,563911),
(956852,502490),
(702223,514032),
(404943,535955),
(178880,572152),
(689477,514734),
(691351,514630),
(866669,506128),
(370561,539656),
(739805,512051),
(71060,619441),
(624861,518534),
(261660,554714),
(366137,540160),
(166054,575698),
(601878,519990),
(153445,579501),
(279899,551729),
(379166,538691),
(423209,534125),
(675310,515526),
(145641,582050),
(691353,514627),
(917468,504026),
(284778,550976),
(81040,612235),
(161699,576978),
(616394,519057),
(767490,510661),
(156896,578431),
(427408,533714),
(254849,555884),
(737217,512182),
(897133,504851),
(203815,566051),
(270822,553189),
(135854,585475),
(778805,510111),
(784373,509847),
(305426,547921),
(733418,512375),
(732087,512448),
(540668,524215),
(702898,513996),
(628057,518328),
(640280,517587),
(422405,534204),
(10604,746569),
(746038,511733),
(839808,507293),
(457417,530938),
(479030,529064),
(341758,543090),
(620223,518824),
(251661,556451),
(561790,522696),
(497733,527521),
(724201,512863),
(489217,528217),
(415623,534867),
(624610,518548),
(847541,506953),
(432295,533249),
(400391,536421),
(961158,502319),
(139173,584284),
(421225,534315),
(579083,521501),
(74274,617000),
(701142,514087),
(374465,539219),
(217814,562985),
(358972,540995),
(88629,607424),
(288597,550389),
(285819,550812),
(538400,524385),
(809930,508645),
(738326,512126),
(955461,502535),
(163829,576343),
(826475,507891),
(376488,538987),
(102234,599905),
(114650,594002),
(52815,636341),
(434037,533082),
(804744,508880),
(98385,601905),
(856620,506559),
(220057,562517),
(844734,507078),
(150677,580387),
(558697,522917),
(621751,518719),
(207067,565321),
(135297,585677),
(932968,503404),
(604456,519822),
(579728,521462),
(244138,557813),
(706487,513800),
(711627,513523),
(853833,506674),
(497220,527562),
(59428,629511),
(564845,522486),
(623621,518603),
(242689,558077),
(125091,589591),
(363819,540432),
(686453,514901),
(656813,516594),
(489901,528155),
(386380,537905),
(542819,524052),
(243987,557841),
(693412,514514),
(488484,528271),
(896331,504881),
(336730,543721),
(728298,512647),
(604215,519840),
(153729,579413),
(595687,520398),
(540360,524240),
(245779,557511),
(924873,503730),
(509628,526577),
(528523,525122),
(3509,847707),
(522756,525555),
(895447,504922),
(44840,646067),
(45860,644715),
(463487,530404),
(398164,536654),
(894483,504959),
(619415,518874),
(966306,502129),
(990922,501212),
(835756,507474),
(548881,523618),
(453578,531282),
(474993,529410),
(80085,612879),
(737091,512193),
(50789,638638),
(979768,501620),
(792018,509483),
(665001,516122),
(86552,608694),
(462772,530469),
(589233,520821),
(891694,505072),
(592605,520594),
(209645,564741),
(42531,649269),
(554376,523226),
(803814,508929),
(334157,544042),
(175836,572970),
(868379,506051),
(658166,516520),
(278203,551995),
(966198,502126),
(627162,518387),
(296774,549165),
(311803,547027),
(843797,507118),
(702304,514032),
(563875,522553),
(33103,664910),
(191932,568841),
(543514,524006),
(506835,526794),
(868368,506052),
(847025,506971),
(678623,515342),
(876139,505726),
(571997,521984),
(598632,520198),
(213590,563892),
(625404,518497),
(726508,512738),
(689426,514738),
(332495,544264),
(411366,535302),
(242546,558110),
(315209,546555),
(797544,509219),
(93889,604371),
(858879,506454),
(124906,589666),
(449072,531693),
(235960,559345),
(642403,517454),
(720567,513047),
(705534,513858),
(603692,519870),
(488137,528302),
(157370,578285),
(63515,625730),
(666326,516041),
(619226,518883),
(443613,532186),
(597717,520257),
(96225,603069),
(86940,608450),
(40725,651929),
(460976,530625),
(268875,553508),
(270671,553214),
(363254,540500),
(384248,538137),
(762889,510892),
(377941,538833),
(278878,551890),
(176615,572755),
(860008,506412),
(944392,502967),
(608395,519571),
(225283,561450),
(45095,645728),
(333798,544090),
(625733,518476),
(995584,501037),
(506135,526853),
(238050,558952),
(557943,522972),
(530978,524938),
(634244,517949),
(177168,572616),
(85200,609541),
(953043,502630),
(523661,525484),
(999295,500902),
(840803,507246),
(961490,502312),
(471747,529685),
(380705,538523),
(911180,504275),
(334149,544046),
(478992,529065),
(325789,545133),
(335884,543826),
(426976,533760),
(749007,511582),
(667067,516000),
(607586,519623),
(674054,515599),
(188534,569675),
(565185,522464),
(172090,573988),
(87592,608052),
(907432,504424),
(8912,760841),
(928318,503590),
(757917,511138),
(718693,513153),
(315141,546566),
(728326,512645),
(353492,541647),
(638429,517695),
(628892,518280),
(877286,505672),
(620895,518778),
(385878,537959),
(423311,534113),
(633501,517997),
(884833,505360),
(883402,505416),
(999665,500894),
(708395,513697),
(548142,523667),
(756491,511205),
(987352,501340),
(766520,510705),
(591775,520647),
(833758,507563),
(843890,507108),
(925551,503698),
(74816,616598),
(646942,517187),
(354923,541481),
(256291,555638),
(634470,517942),
(930904,503494),
(134221,586071),
(282663,551304),
(986070,501394),
(123636,590176),
(123678,590164),
(481717,528841),
(423076,534137),
(866246,506145),
(93313,604697),
(783632,509880),
(317066,546304),
(502977,527103),
(141272,583545),
(71708,618938),
(617748,518975),
(581190,521362),
(193824,568382),
(682368,515131),
(352956,541712),
(351375,541905),
(505362,526909),
(905165,504518),
(128645,588188),
(267143,553787),
(158409,577965),
(482776,528754),
(628896,518282),
(485233,528547),
(563606,522574),
(111001,595655),
(115920,593445),
(365510,540237),
(959724,502374),
(938763,503184),
(930044,503520),
(970959,501956),
(913658,504176),
(68117,621790),
(989729,501253),
(567697,522288),
(820427,508163),
(54236,634794),
(291557,549938),
(124961,589646),
(403177,536130),
(405421,535899),
(410233,535417),
(815111,508403),
(213176,563974),
(83099,610879),
(998588,500934),
(513640,526263),
(129817,587733),
(1820,921851),
(287584,550539),
(299160,548820),
(860621,506386),
(529258,525059),
(586297,521017),
(953406,502616),
(441234,532410),
(986217,501386),
(781938,509957),
(461247,530595),
(735424,512277),
(146623,581722),
(839838,507288),
(510667,526494),
(935085,503327),
(737523,512167),
(303455,548204),
(992779,501145),
(60240,628739),
(939095,503174),
(794368,509370),
(501825,527189),
(459028,530798),
(884641,505363),
(512287,526364),
(835165,507499),
(307723,547590),
(160587,577304),
(735043,512300),
(493289,527887),
(110717,595785),
(306480,547772),
(318593,546089),
(179810,571911),
(200531,566799),
(314999,546580),
(197020,567622),
(301465,548487),
(237808,559000),
(131944,586923),
(882527,505449),
(468117,530003),
(711319,513541),
(156240,578628),
(965452,502162),
(992756,501148),
(437959,532715),
(739938,512046),
(614249,519196),
(391496,537356),
(62746,626418),
(688215,514806),
(75501,616091),
(883573,505412),
(558824,522910),
(759371,511061),
(173913,573489),
(891351,505089),
(727464,512693),
(164833,576051),
(812317,508529),
(540320,524243),
(698061,514257),
(69149,620952),
(471673,529694),
(159092,577753),
(428134,533653),
(89997,606608),
(711061,513557),
(779403,510081),
(203327,566155),
(798176,509187),
(667688,515963),
(636120,517833),
(137410,584913),
(217615,563034),
(556887,523038),
(667229,515991),
(672276,515708),
(325361,545187),
(172115,573985),
(13846,725685)]

#{519432:525806,
# 632382:518061,
# 78864:613712,
# 466580:530130,
# 780495:510032,
# 525895:525320,
# 15991:714883,
# 960290:502358,
# 760018:511029,
# 166800:575487,
# 210884:564478,
# 555151:523163,
# 681146:515199,
# 563395:522587,
# 738250:512126,
# 923525:503780,
# 595148:520429,
# 177108:572629,
# 750923:511482,
# 440902:532446,
# 881418:505504,
# 422489:534197,
# 979858:501616,
# 685893:514935,
# 747477:511661,
# 167214:575367,
# 234140:559696,
# 940238:503122,
# 728969:512609,
# 232083:560102,
# 900971:504694,
# 688801:514772,
# 189664:569402,
# 891022:505104,
# 445689:531996,
# 119570:591871,
# 821453:508118,
# 371084:539600,
# 911745:504251,
# 623655:518600,
# 144361:582486,
# 352442:541775,
# 420726:534367,
# 295298:549387,
# 6530:787777,
# 468397:529976,
# 672336:515696,
# 431861:533289,
# 84228:610150,
# 805376:508857,
# 444409:532117,
# 33833:663511,
# 381850:538396,
# 402931:536157,
# 92901:604930,
# 304825:548004,
# 731917:512452,
# 753734:511344,
# 51894:637373,
# 151578:580103,
# 295075:549421,
# 303590:548183,
# 333594:544123,
# 683952:515042,
# 60090:628880,
# 951420:502692,
# 28335:674991,
# 714940:513349,
# 343858:542826,
# 549279:523586,
# 804571:508887,
# 260653:554881,
# 291399:549966,
# 402342:536213,
# 408889:535550,
# 40328:652524,
# 375856:539061,
# 768907:510590,
# 165993:575715,
# 976327:501755,
# 898500:504795,
# 360404:540830,
# 478714:529095,
# 694144:514472,
# 488726:528258,
# 841380:507226,
# 328012:544839,
# 22389:690868,
# 604053:519852,
# 329514:544641,
# 772965:510390,
# 492798:527927,
# 30125:670983,
# 895603:504906,
# 450785:531539,
# 840237:507276,
# 380711:538522,
# 63577:625673,
# 76801:615157,
# 502694:527123,
# 597706:520257,
# 310484:547206,
# 944468:502959,
# 121283:591152,
# 451131:531507,
# 566499:522367,
# 425373:533918,
# 40240:652665,
# 39130:654392,
# 714926:513355,
# 469219:529903,
# 806929:508783,
# 287970:550487,
# 92189:605332,
# 103841:599094,
# 671839:515725,
# 452048:531421,
# 987837:501323,
# 935192:503321,
# 88585:607450,
# 613883:519216,
# 144551:582413,
# 647359:517155,
# 213902:563816,
# 184120:570789,
# 258126:555322,
# 502546:527130,
# 407655:535678,
# 401528:536306,
# 477490:529193,
# 841085:507237,
# 732831:512408,
# 833000:507595,
# 904694:504542,
# 581435:521348,
# 455545:531110,
# 873558:505829,
# 94916:603796,
# 720176:513068,
# 545034:523891,
# 246348:557409,
# 556452:523079,
# 832015:507634,
# 173663:573564,
# 502634:527125,
# 250732:556611,
# 569786:522139,
# 216919:563178,
# 521815:525623,
# 92304:605270,
# 164446:576167,
# 753413:511364,
# 11410:740712,
# 448845:531712,
# 925072:503725,
# 564888:522477,
# 7062:780812,
# 641155:517535,
# 738878:512100,
# 636204:517828,
# 372540:539436,
# 443162:532237,
# 571192:522042,
# 655350:516680,
# 299741:548735,
# 581914:521307,
# 965471:502156,
# 513441:526277,
# 808682:508700,
# 237589:559034,
# 543300:524025,
# 804712:508889,
# 247511:557192,
# 543486:524008,
# 504383:526992,
# 326529:545039,
# 792493:509458,
# 86033:609017,
# 126554:589005,
# 579379:521481,
# 948026:502823,
# 404777:535969,
# 265767:554022,
# 266876:553840,
# 46631:643714,
# 492397:527958,
# 856106:506581,
# 795757:509305,
# 748946:511584,
# 294694:549480,
# 409781:535463,
# 775887:510253,
# 543747:523991,
# 210592:564536,
# 517119:525990,
# 520253:525751,
# 247926:557124,
# 592141:520626,
# 346580:542492,
# 544969:523902,
# 506501:526817,
# 244520:557738,
# 144745:582349,
# 69274:620858,
# 292620:549784,
# 926027:503687,
# 736320:512225,
# 515528:526113,
# 407549:535688,
# 848089:506927,
# 24141:685711,
# 9224:757964,
# 980684:501586,
# 175259:573121,
# 489160:528216,
# 878970:505604,
# 969546:502002,
# 525207:525365,
# 690461:514675,
# 156510:578551,
# 659778:516426,
# 468739:529945,
# 765252:510770,
# 76703:615230,
# 165151:575959,
# 29779:671736,
# 928865:503569,
# 577538:521605,
# 927555:503618,
# 185377:570477,
# 974756:501809,
# 800130:509093,
# 217016:563153,
# 365709:540216,
# 774508:510320,
# 588716:520851,
# 631673:518104,
# 954076:502590,
# 777828:510161,
# 990659:501222,
# 597799:520254,
# 786905:509727,
# 512547:526348,
# 756449:511212,
# 869787:505988,
# 653747:516779,
# 84623:609900,
# 839698:507295,
# 30159:670909,
# 797275:509234,
# 678136:515373,
# 897144:504851,
# 989554:501263,
# 413292:535106,
# 55297:633667,
# 788650:509637,
# 486748:528417,
# 150724:580377,
# 56434:632490,
# 77207:614869,
# 588631:520859,
# 611619:519367,
# 100006:601055,
# 528924:525093,
# 190225:569257,
# 851155:506789,
# 682593:515114,
# 613043:519275,
# 514673:526183,
# 877634:505655,
# 878905:505602,
# 1926:914951,
# 613245:519259,
# 152481:579816,
# 841774:507203,
# 71060:619442,
# 865335:506175,
# 90244:606469,
# 302156:548388,
# 399059:536557,
# 478465:529113,
# 558601:522925,
# 69132:620966,
# 267663:553700,
# 988276:501310,
# 378354:538787,
# 529909:525014,
# 161733:576968,
# 758541:511109,
# 823425:508024,
# 149821:580667,
# 269258:553438,
# 481152:528891,
# 120871:591322,
# 972322:501901,
# 981350:501567,
# 676129:515483,
# 950860:502717,
# 119000:592114,
# 392252:537272,
# 191618:568919,
# 946699:502874,
# 289555:550247,
# 799322:509139,
# 703886:513942,
# 194812:568143,
# 261823:554685,
# 203052:566221,
# 217330:563093,
# 734748:512313,
# 391759:537328,
# 807052:508777,
# 564467:522510,
# 59186:629748,
# 113447:594545,
# 518063:525916,
# 905944:504492,
# 613922:519213,
# 439093:532607,
# 445946:531981,
# 230530:560399,
# 297887:549007,
# 459029:530797,
# 403692:536075,
# 855118:506616,
# 963127:502245,
# 841711:507208,
# 407411:535699,
# 924729:503735,
# 914823:504132,
# 333725:544101,
# 176345:572832,
# 912507:504225,
# 411273:535308,
# 259774:555036,
# 632853:518038,
# 119723:591801,
# 163902:576321,
# 22691:689944,
# 402427:536212,
# 175769:572988,
# 837260:507402,
# 603432:519893,
# 313679:546767,
# 538165:524394,
# 549026:523608,
# 61083:627945,
# 898345:504798,
# 992556:501153,
# 369999:539727,
# 32847:665404,
# 891292:505088,
# 152715:579732,
# 824104:507997,
# 234057:559711,
# 730507:512532,
# 960529:502340,
# 388395:537687,
# 958170:502437,
# 57105:631806,
# 186025:570311,
# 993043:501133,
# 576770:521664,
# 215319:563513,
# 927342:503628,
# 521353:525666,
# 39563:653705,
# 752516:511408,
# 110755:595770,
# 309749:547305,
# 374379:539224,
# 919184:503952,
# 990652:501226,
# 647780:517135,
# 187177:570017,
# 168938:574877,
# 649558:517023,
# 278126:552016,
# 162039:576868,
# 658512:516499,
# 498115:527486,
# 896583:504868,
# 561170:522740,
# 747772:511647,
# 775093:510294,
# 652081:516882,
# 724905:512824,
# 499707:527365,
# 47388:642755,
# 646668:517204,
# 571700:522007,
# 180430:571747,
# 710015:513617,
# 435522:532941,
# 98137:602041,
# 759176:511070,
# 486124:528467,
# 526942:525236,
# 878921:505604,
# 408313:535602,
# 926980:503640,
# 882353:505459,
# 566887:522345,
# 3326:853312,
# 911981:504248,
# 416309:534800,
# 392991:537199,
# 622829:518651,
# 148647:581055,
# 496483:527624,
# 666314:516044,
# 48562:641293,
# 672618:515684,
# 443676:532187,
# 274065:552661,
# 265386:554079,
# 347668:542358,
# 31816:667448,
# 181575:571446,
# 961289:502320,
# 365689:540214,
# 987950:501317,
# 932299:503440,
# 27388:677243,
# 746701:511701,
# 492258:527969,
# 147823:581323,
# 57918:630985,
# 838849:507333,
# 678038:515375,
# 27852:676130,
# 850241:506828,
# 818403:508253,
# 131717:587014,
# 850216:506834,
# 904848:504529,
# 189758:569380,
# 392845:537217,
# 470876:529761,
# 925353:503711,
# 285431:550877,
# 454098:531234,
# 823910:508003,
# 318493:546112,
# 766067:510730,
# 261277:554775,
# 421530:534289,
# 694130:514478,
# 120439:591498,
# 213308:563949,
# 854063:506662,
# 365255:540263,
# 165437:575872,
# 662240:516281,
# 289970:550181,
# 847977:506933,
# 546083:523816,
# 413252:535113,
# 975829:501767,
# 361540:540701,
# 235522:559435,
# 224643:561577,
# 736350:512229,
# 328303:544808,
# 35022:661330,
# 307838:547578,
# 474366:529458,
# 873755:505819,
# 73978:617220,
# 827387:507845,
# 670830:515791,
# 326511:545034,
# 309909:547285,
# 400970:536363,
# 884827:505352,
# 718307:513175,
# 28462:674699,
# 599384:520150,
# 253565:556111,
# 284009:551093,
# 343403:542876,
# 446557:531921,
# 992372:501160,
# 961601:502308,
# 696629:514342,
# 919537:503945,
# 894709:504944,
# 892201:505051,
# 358160:541097,
# 448503:531745,
# 832156:507636,
# 920045:503924,
# 926137:503675,
# 416754:534757,
# 254422:555966,
# 92498:605151,
# 826833:507873,
# 660716:516371,
# 689335:514746,
# 160045:577467,
# 814642:508425,
# 969939:501993,
# 242856:558047,
# 76302:615517,
# 472083:529653,
# 587101:520964,
# 99066:601543,
# 498005:527503,
# 709800:513624,
# 708000:513716,
# 20171:698134,
# 285020:550936,
# 266564:553891,
# 981563:501557,
# 846502:506991,
# 334:1190800,
# 209268:564829,
# 9844:752610,
# 996519:501007,
# 410059:535426,
# 432931:533188,
# 848012:506929,
# 966803:502110,
# 983434:501486,
# 160700:577267,
# 504374:526989,
# 832061:507640,
# 392825:537214,
# 443842:532165,
# 440352:532492,
# 745125:511776,
# 13718:726392,
# 661753:516312,
# 70500:619875,
# 436952:532814,
# 424724:533973,
# 21954:692224,
# 262490:554567,
# 716622:513264,
# 907584:504425,
# 60086:628882,
# 837123:507412,
# 971345:501940,
# 947162:502855,
# 139920:584021,
# 68330:621624,
# 666452:516038,
# 731446:512481,
# 953350:502619,
# 183157:571042,
# 845400:507045,
# 651548:516910,
# 20399:697344,
# 861779:506331,
# 629771:518229,
# 801706:509026,
# 189207:569512,
# 737501:512168,
# 719272:513115,
# 479285:529045,
# 136046:585401,
# 896746:504860,
# 891735:505067,
# 684771:514999,
# 865309:506184,
# 379066:538702,
# 503117:527090,
# 621780:518717,
# 209518:564775,
# 677135:515423,
# 987500:501340,
# 197049:567613,
# 329315:544673,
# 236756:559196,
# 357092:541226,
# 520440:525733,
# 213471:563911,
# 956852:502490,
# 702223:514032,
# 404943:535955,
# 178880:572152,
# 689477:514734,
# 691351:514630,
# 866669:506128,
# 370561:539656,
# 739805:512051,
# 71060:619441,
# 624861:518534,
# 261660:554714,
# 366137:540160,
# 166054:575698,
# 601878:519990,
# 153445:579501,
# 279899:551729,
# 379166:538691,
# 423209:534125,
# 675310:515526,
# 145641:582050,
# 691353:514627,
# 917468:504026,
# 284778:550976,
# 81040:612235,
# 161699:576978,
# 616394:519057,
# 767490:510661,
# 156896:578431,
# 427408:533714,
# 254849:555884,
# 737217:512182,
# 897133:504851,
# 203815:566051,
# 270822:553189,
# 135854:585475,
# 778805:510111,
# 784373:509847,
# 305426:547921,
# 733418:512375,
# 732087:512448,
# 540668:524215,
# 702898:513996,
# 628057:518328,
# 640280:517587,
# 422405:534204,
# 10604:746569,
# 746038:511733,
# 839808:507293,
# 457417:530938,
# 479030:529064,
# 341758:543090,
# 620223:518824,
# 251661:556451,
# 561790:522696,
# 497733:527521,
# 724201:512863,
# 489217:528217,
# 415623:534867,
# 624610:518548,
# 847541:506953,
# 432295:533249,
# 400391:536421,
# 961158:502319,
# 139173:584284,
# 421225:534315,
# 579083:521501,
# 74274:617000,
# 701142:514087,
# 374465:539219,
# 217814:562985,
# 358972:540995,
# 88629:607424,
# 288597:550389,
# 285819:550812,
# 538400:524385,
# 809930:508645,
# 738326:512126,
# 955461:502535,
# 163829:576343,
# 826475:507891,
# 376488:538987,
# 102234:599905,
# 114650:594002,
# 52815:636341,
# 434037:533082,
# 804744:508880,
# 98385:601905,
# 856620:506559,
# 220057:562517,
# 844734:507078,
# 150677:580387,
# 558697:522917,
# 621751:518719,
# 207067:565321,
# 135297:585677,
# 932968:503404,
# 604456:519822,
# 579728:521462,
# 244138:557813,
# 706487:513800,
# 711627:513523,
# 853833:506674,
# 497220:527562,
# 59428:629511,
# 564845:522486,
# 623621:518603,
# 242689:558077,
# 125091:589591,
# 363819:540432,
# 686453:514901,
# 656813:516594,
# 489901:528155,
# 386380:537905,
# 542819:524052,
# 243987:557841,
# 693412:514514,
# 488484:528271,
# 896331:504881,
# 336730:543721,
# 728298:512647,
# 604215:519840,
# 153729:579413,
# 595687:520398,
# 540360:524240,
# 245779:557511,
# 924873:503730,
# 509628:526577,
# 528523:525122,
# 3509:847707,
# 522756:525555,
# 895447:504922,
# 44840:646067,
# 45860:644715,
# 463487:530404,
# 398164:536654,
# 894483:504959,
# 619415:518874,
# 966306:502129,
# 990922:501212,
# 835756:507474,
# 548881:523618,
# 453578:531282,
# 474993:529410,
# 80085:612879,
# 737091:512193,
# 50789:638638,
# 979768:501620,
# 792018:509483,
# 665001:516122,
# 86552:608694,
# 462772:530469,
# 589233:520821,
# 891694:505072,
# 592605:520594,
# 209645:564741,
# 42531:649269,
# 554376:523226,
# 803814:508929,
# 334157:544042,
# 175836:572970,
# 868379:506051,
# 658166:516520,
# 278203:551995,
# 966198:502126,
# 627162:518387,
# 296774:549165,
# 311803:547027,
# 843797:507118,
# 702304:514032,
# 563875:522553,
# 33103:664910,
# 191932:568841,
# 543514:524006,
# 506835:526794,
# 868368:506052,
# 847025:506971,
# 678623:515342,
# 876139:505726,
# 571997:521984,
# 598632:520198,
# 213590:563892,
# 625404:518497,
# 726508:512738,
# 689426:514738,
# 332495:544264,
# 411366:535302,
# 242546:558110,
# 315209:546555,
# 797544:509219,
# 93889:604371,
# 858879:506454,
# 124906:589666,
# 449072:531693,
# 235960:559345,
# 642403:517454,
# 720567:513047,
# 705534:513858,
# 603692:519870,
# 488137:528302,
# 157370:578285,
# 63515:625730,
# 666326:516041,
# 619226:518883,
# 443613:532186,
# 597717:520257,
# 96225:603069,
# 86940:608450,
# 40725:651929,
# 460976:530625,
# 268875:553508,
# 270671:553214,
# 363254:540500,
# 384248:538137,
# 762889:510892,
# 377941:538833,
# 278878:551890,
# 176615:572755,
# 860008:506412,
# 944392:502967,
# 608395:519571,
# 225283:561450,
# 45095:645728,
# 333798:544090,
# 625733:518476,
# 995584:501037,
# 506135:526853,
# 238050:558952,
# 557943:522972,
# 530978:524938,
# 634244:517949,
# 177168:572616,
# 85200:609541,
# 953043:502630,
# 523661:525484,
# 999295:500902,
# 840803:507246,
# 961490:502312,
# 471747:529685,
# 380705:538523,
# 911180:504275,
# 334149:544046,
# 478992:529065,
# 325789:545133,
# 335884:543826,
# 426976:533760,
# 749007:511582,
# 667067:516000,
# 607586:519623,
# 674054:515599,
# 188534:569675,
# 565185:522464,
# 172090:573988,
# 87592:608052,
# 907432:504424,
# 8912:760841,
# 928318:503590,
# 757917:511138,
# 718693:513153,
# 315141:546566,
# 728326:512645,
# 353492:541647,
# 638429:517695,
# 628892:518280,
# 877286:505672,
# 620895:518778,
# 385878:537959,
# 423311:534113,
# 633501:517997,
# 884833:505360,
# 883402:505416,
# 999665:500894,
# 708395:513697,
# 548142:523667,
# 756491:511205,
# 987352:501340,
# 766520:510705,
# 591775:520647,
# 833758:507563,
# 843890:507108,
# 925551:503698,
# 74816:616598,
# 646942:517187,
# 354923:541481,
# 256291:555638,
# 634470:517942,
# 930904:503494,
# 134221:586071,
# 282663:551304,
# 986070:501394,
# 123636:590176,
# 123678:590164,
# 481717:528841,
# 423076:534137,
# 866246:506145,
# 93313:604697,
# 783632:509880,
# 317066:546304,
# 502977:527103,
# 141272:583545,
# 71708:618938,
# 617748:518975,
# 581190:521362,
# 193824:568382,
# 682368:515131,
# 352956:541712,
# 351375:541905,
# 505362:526909,
# 905165:504518,
# 128645:588188,
# 267143:553787,
# 158409:577965,
# 482776:528754,
# 628896:518282,
# 485233:528547,
# 563606:522574,
# 111001:595655,
# 115920:593445,
# 365510:540237,
# 959724:502374,
# 938763:503184,
# 930044:503520,
# 970959:501956,
# 913658:504176,
# 68117:621790,
# 989729:501253,
# 567697:522288,
# 820427:508163,
# 54236:634794,
# 291557:549938,
# 124961:589646,
# 403177:536130,
# 405421:535899,
# 410233:535417,
# 815111:508403,
# 213176:563974,
# 83099:610879,
# 998588:500934,
# 513640:526263,
# 129817:587733,
# 1820:921851,
# 287584:550539,
# 299160:548820,
# 860621:506386,
# 529258:525059,
# 586297:521017,
# 953406:502616,
# 441234:532410,
# 986217:501386,
# 781938:509957,
# 461247:530595,
# 735424:512277,
# 146623:581722,
# 839838:507288,
# 510667:526494,
# 935085:503327,
# 737523:512167,
# 303455:548204,
# 992779:501145,
# 60240:628739,
# 939095:503174,
# 794368:509370,
# 501825:527189,
# 459028:530798,
# 884641:505363,
# 512287:526364,
# 835165:507499,
# 307723:547590,
# 160587:577304,
# 735043:512300,
# 493289:527887,
# 110717:595785,
# 306480:547772,
# 318593:546089,
# 179810:571911,
# 200531:566799,
# 314999:546580,
# 197020:567622,
# 301465:548487,
# 237808:559000,
# 131944:586923,
# 882527:505449,
# 468117:530003,
# 711319:513541,
# 156240:578628,
# 965452:502162,
# 992756:501148,
# 437959:532715,
# 739938:512046,
# 614249:519196,
# 391496:537356,
# 62746:626418,
# 688215:514806,
# 75501:616091,
# 883573:505412,
# 558824:522910,
# 759371:511061,
# 173913:573489,
# 891351:505089,
# 727464:512693,
# 164833:576051,
# 812317:508529,
# 540320:524243,
# 698061:514257,
# 69149:620952,
# 471673:529694,
# 159092:577753,
# 428134:533653,
# 89997:606608,
# 711061:513557,
# 779403:510081,
# 203327:566155,
# 798176:509187,
# 667688:515963,
# 636120:517833,
# 137410:584913,
# 217615:563034,
# 556887:523038,
# 667229:515991,
# 672276:515708,
# 325361:545187,
# 172115:573985,
# 13846:725685,
# }

# u_of_k = sum(nums_dict.keys()) // len(nums_dict.keys())
# u_of_v = sum(nums_dict.values()) // len(nums_dict.values())
# print("mean k: ", u_of_k, " mean v: ", u_of_v)

# meu_of_k = max(nums_dict.keys()) - min(nums_dict.keys())
# meu_of_v = max(nums_dict.values()) - min(nums_dict.values())
# print("meu k: ", meu_of_k,"meu v", meu_of_v)

# def std(x, dict_):
# 	if dict_ == 'v':
# 		return math.sqrt((sum([i-u_of_v for i in nums_dict.values()])**2) // len(nums_dict.values()))
# 	return math.sqrt((sum([i-u_of_k for i in nums_dict.keys()]) ** 2) // len(nums_dict.keys()))

# def z_score(x, dict_):
# 	if dict_ == 'v':
# 		print(abs((x - u_of_v) // std(x, dict_)))
# 		return abs((x - u_of_v) // std(x, dict_))
# 	print(abs((x - u_of_k) // std(x, dict_)))
# 	return abs((x - u_of_k) // std(x, dict_))


val = 0
key = 0
big = 0
for v in nums_dict:
	# print(v)
	# if len(str(k)) > 5 and len(str(v)) > 5:
	# ans = abs((z_score(k, 'k'))**(z_score(v, 'v')))
	ans = (v[0]//100) ** (v[1]//100)
	# print(ans)
	if ans > big:
		big = ans
		val = v[0]
		key = v[1]
		print(key, val)
print("got it ", key, val)

		# print(kv, max(nums_dict.values()))

	# if  local > max_:
	# 		max_ = local
	# 		key = k
	# 		val = v 
	

# print(max_)
# print(key)

# print(val)
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> for i in range (-90, 90):
	print (i)

	
-90
-89
-88
-87
-86
-85
-84
-83
-82
-81
-80
-79
-78
-77
-76
-75
-74
-73
-72
-71
-70
-69
-68
-67
-66
-65
-64
-63
-62
-61
-60
-59
-58
-57
-56
-55
-54
-53
-52
-51
-50
-49
-48
-47
-46
-45
-44
-43
-42
-41
-40
-39
-38
-37
-36
-35
-34
-33
-32
-31
-30
-29
-28
-27
-26
-25
-24
-23
-22
-21
-20
-19
-18
-17
-16
-15
-14
-13
-12
-11
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
>>> for i in range (123, 1234, 6):
	print (i)

	
123
129
135
141
147
153
159
165
171
177
183
189
195
201
207
213
219
225
231
237
243
249
255
261
267
273
279
285
291
297
303
309
315
321
327
333
339
345
351
357
363
369
375
381
387
393
399
405
411
417
423
429
435
441
447
453
459
465
471
477
483
489
495
501
507
513
519
525
531
537
543
549
555
561
567
573
579
585
591
597
603
609
615
621
627
633
639
645
651
657
663
669
675
681
687
693
699
705
711
717
723
729
735
741
747
753
759
765
771
777
783
789
795
801
807
813
819
825
831
837
843
849
855
861
867
873
879
885
891
897
903
909
915
921
927
933
939
945
951
957
963
969
975
981
987
993
999
1005
1011
1017
1023
1029
1035
1041
1047
1053
1059
1065
1071
1077
1083
1089
1095
1101
1107
1113
1119
1125
1131
1137
1143
1149
1155
1161
1167
1173
1179
1185
1191
1197
1203
1209
1215
1221
1227
1233
>>> result = 0
>>> for element in range (5):
	result  = result + element
	print ("The sum is: " + str(result))

	
The sum is: 0
The sum is: 1
The sum is: 3
The sum is: 6
The sum is: 10
>>> result = 0
>>> for element in range (5, 1, -1):
	result = result + element
	print ("The sume is: " + str(result))

	
The sume is: 5
The sume is: 9
The sume is: 12
The sume is: 14
>>> result = 0
>>> for element in range (0, 8, 2):
	result = result + element
	print ("The sum is: " + str(result))

	
The sum is: 0
The sum is: 2
The sum is: 6
The sum is: 12
>>> result = 0
>>> size = 5
>>> for element in range (size):
	result = result + element
	print ("When size = " + str(size) + "result is" + str(result))

	
When size = 5result is0
When size = 5result is1
When size = 5result is3
When size = 5result is6
When size = 5result is10
>>> for element in range (size):
	result = result + element
	print ("When size = " + str(size) + " result is" + str(result))

	
When size = 5 result is10
When size = 5 result is11
When size = 5 result is13
When size = 5 result is16
When size = 5 result is20
>>> for element in range (size):
	result = result + element
	print ("When size = " + str(size) + " result is " + str(result))

	
When size = 5 result is 20
When size = 5 result is 21
When size = 5 result is 23
When size = 5 result is 26
When size = 5 result is 30
>>> 

# -*- coding: utf-8 -*-      #������������� ����� utf-8

from random import
player_score=0              #���� ��� ������=0           
computer_score=0              #���� ��� ����������=0 
start()
def hangman(hangman):        #�������� ��� ������ hangman
   graphic=[             #����� ��������
   

   "--------
    |      |
    | 
    |
    |
    |
	
    "
	
    "--------
     |      |
     |      �
     |
     |
     |
     "
	

def start():                   #�������� �� �� ����� � ������ ������

   print "��� �� ��������� �������"
   print "E���� �������; ��������"
   while game(): 
      pass
   score()
#���� �� �������� ���������� �������� �� ����    

def game():                #�������� ��� �� �� ���������  � ������ ��������

   dictionary=["gnu","kernel","linux","unbuntu"]    #������
   word=choice(dictionary)                            #� ���� ��� �� �������� ����� ����� ������� ��� �� ������ ��� 
   word_length=len(word)                              #�� ������ ��� ����� =������ ��� �����
   clue=word_length * ["_"]                           #�� ���� = �� �� ������ ��� ����� * _
   tries=8                                          # ���� �������� 8 �����������
   letters_tried= " "                             # �������� ��� ����� 
   guesses=0                                      # ��������
   letters_right=0                                # ����� ��������
   letters_wrong=0                                   # ����� ��������
   global computer_score , player_score                 
   
def guess_letter():                        #�������� ��� ������ �������� ��� �������
   print                                   #�� ���������
   letter=raw_input("���� ������")            # ��� ���� �� ����� ������
   letter.strip()                           #�� ��������� �� ���� ���� � ���� �� ������ ��� ����� � �������
   letter.lower()                          #�� ����� ��� �� �������� ��� ����� � ������� ����� 
   word.lower                             #�� ���������� ��� ������ �� ����� ��������
   retuern letter                        #�� ���������� ���� ���� 
   
While (letters_wrong!=tries) and         #��� �� ������ ��� ����� ����� ����� ��� ������ �� ��� 8���������� ����
("",join (clue)!=word):              #���� ������ ��� ����
   letter=guess_letter()             #�� ������ = �� �� ������ ��� �������
   if len(letter==1) and               #������� �� ����� ���� ��� �����
   letter.isalpha():                  #��� ������� ��� �� ������ ��� ����� ����� ���� ��� ��������
      
	  if letters_tries.fing(letter)!=1:        #��� �� ������ ��� �����, �� ���� ���� �����
	    print"�� ������ ���� ����" ,letter     #�������� ��� ..... , ��� �� ������ ����
	  else:                                        #������	
	    letter_tried=letters_tries + letter      #�� ����� �� �� �������� ��� ����� � �������=�� ��� letters ��� ����� + �� ��������� 
		first_index_index=-1:                 
		    letter_wrong+=1                    #��� ����� ����� ������ +1 ���� ����� 
		       print"������ ����� ������"
		    else:
			   print"������ ��� ������" ,letter
			for i in range(word_lenght)           #��� i ��� �����(������ ��� �����)
				   if letter=word[i]:              #��� �� ������ =�� ��� ���� i
				      clue[i]=letter             #�� ������� i = �� �� ������
  	               else:
	                 print"������� ���� ������"
		hangman(letters_wrong)                    
        print" ".join(clue)
		print"��������� ���� �� ��������" ,letters_tried      #�������� ��� .... , ��� �� ������� ��� ���� ���������
		if letters_tries==tries:                 #��� �� �� ����������� ��� ����� �������� ������= �� �� ��� 8 ����� ���������� ��� ����
		   print"������ ����"                  #�������� ������
		   computer_score+=1              #���� ���������� +1
		   break                            #�������
		if "" join(clue)==word:
		   print"������� ����"
		   player_score+=1          #���� ������ +1
		   break                            #�������
		return play_again()        #��������� ���� ��������� ����� ���� 
		
	def play_again():
	   answer=raw input("��� �� ������� ���� ;�/�")
	   if answer in("N","n","nai"):    #��� � ������� ����� ���� ��� ���� 
	       return answer          
		else:                    #������
		   print"��	��������� ��� �������".   
		    
	def score():
	  global player_score, computer_score
	  print ������� ,player_score
	  print PC ,computer_score
	  
	return
   


   
# Chapter 10, Lab 03
# 교재에는 답이 적혀있지만, 답을 안 보고 혼자 만들어보기
# 노트(note)를 정리하는 프로그램
# 사용자는 노트에 콘텐츠를 적을 수 있음
# 노트는 노트북(notebook)에 삽입 됨
# 노트북은 타이틀(title)이 있음
# 노트북은 노트가 삽입될 때 페이지를 생성, 최대 300페이지까지 저장 가능
# 300페이지를 넘기면 노트를 더는 삽입하지 못함

# 노트 한 페이지에는 내용을 넣을 수도 있고, 지울 수도 있고, 수정할 수도 있음
# 노트가 노트북에 삽입되면 노트북의 페이지가 +1
# 노트북이 300페이지가 되면 노트를 삽입 불가
# 노트북에 있는 내용을 초기화 가능
# 노트북에 있는 일정 페이지만 초기화 가능
# 노트북에는 타이틀이 있음
# 노트 클래스, 노트북 클래스 만들기

# 노트 클래스
    # 노트 생성은 기본
    # 내용 추가 기능
        # 노트라는 리스트에 append
    # 내용 삭제 기능
        # 원하는 내용을 정확히 입력하면 그 부분만 삭제하는 기능
            # 한 케이스만 나와야 하며 두 케이스 이상이 나올 경우 삭제되지 않음
        # 일정 내용의 뒷 부분을 다 삭제하는 기능
            # 한 케이스만 나와야 함
        # 전부 삭제하는 기능
    # 내용 수정 기능
        # 원하는 내용을 정확히 입력하면 그 부분만 수정하는 기능
            # 한 케이스만 나와야 함

# 노트북 클래스
    # 타이틀은 기본 (타이틀은 0페이지라 설정)
    # 노트북 페이지가 추가되는 기능
        # 노트북이 300페이지일 경우 페이지가 추가되지 않음
    # 노트북의 내용을 초기화 하는 기능
        # 노트북의 내용을 타이틀을 제외하고 전부 초기화
    # 노트북에 있는 일정 페이지만 초기화 하는 기능
        # 페이지를 정확히 입력하면 그 페이지가 초기화 됨
            # 딕셔너리 사용
    # 원하는 페이지를 입력하면 그 페이지에 할당된 노트를 볼 수 있는 기능

class Note(object) :
    def __init__(self, contents = None) :   # 처음 내용은 아무것도 없으므로 contents = None
        self.contents = contents

    def __str__(self) :
        return self.contents
    
    def write_note(self, contents) :    # 노트에 내용 추가 기능
        if self.contents == None :
            self.contents = contents
        else :
            self.contents = self.contents + " " + contents
    
    def remove_behind_word(self, word) :    # 노트의 중복되지 않는 특정 단어의 뒤를 지우는 기능
        split_list = self.contents.split()
        if split_list.count(word) == 1 :
            a = len(word)
            while split_list[-1] != word :
                del split_list[-1]
            self.contents = " ".join(split_list)
        elif split_list.count(word) >= 2 :
            print("중복되는 단어입니다.")
        else :
            print("존재하지 않는 단어이거나 마침표를 포함하지 않았습니다.")
            
    
    def remove_selected_word(self, word) :  # 노트의 중복되지 않는 특정 단어를 지우는 기능
        split_list = self.contents.split()
        if split_list.count(word) == 1 :
            split_list.remove(word)
            self.contents = " ".join(split_list)
        elif split_list.count(word) >= 2 :
            print("중복되는 단어입니다.")
        else :
            print("존재하지 않는 단어이거나 마침표를 포함하지 않았습니다.")

    def change_word(self, word, new_word) : # 노트의 중복되지 않는 특정 단어를 수정하는 기능
        split_list = self.contents.split()
        if split_list.count(word) == 1 :
            a = split_list.index(word)
            split_list.remove(word)
            split_list.insert(a, new_word)
            self.contents = " ".join(split_list)
        elif split_list.count(word) >= 2 :
            print("중복되는 단어입니다.")
        else :
            print("존재하지 않는 단어이거나 마침표를 포함하지 않았습니다.")

class Notebook(object) :
    def __init__(self, title) :
        self.title = title
        self.pgnumber = 1
        self.notes = {}
        self.notes[0] = title   # 0페이지는 title
        # from collections import OrderedDict
        # self.notes = OrderedDict()
    
    def add_note(self, note, page = 0) :    # 노트북에 노트를 추가하는 기능
        if self.pgnumber <= 300 :
            if page == 0 :
                while self.pgnumber in self.notes.keys() :  # 해당 페이지에 note의 내용이 추가되지 않았을 때(이미 다른 내용이 있었을 때) 반복
                    self.pgnumber += 1
                self.notes.setdefault(self.pgnumber, note)
                print("%s가 page %d에 삽입되었습니다." % (note, self.pgnumber))
            elif page > 0 and page <= 300 :
                self.notes.setdefault(page, note)
                if self.notes[page] != note :
                    print("해당 페이지는 이미 삽입된 글이 있습니다. 수정을 원하는 경우 remove_page 함수를 사용하여 주십시오.")
                else :
                    print("%s가 page %d에 삽입되었습니다." % (note, page))
            else :
                print("올바른 페이지 범위를 입력하여 주십시오.")
        else :
            print("더 이상 페이지를 추가할 수 없습니다.")

    def remove_all_pages(self) :    # 노트북에 있는 모든 페이지 초기화
        for _ in range(1, 301) :    # title은 남겨두기, title이 0페이지고 300페이지까지 설정 했으므로 301로 끝나는게 맞음
            try :
                del self.notes[_]
            except KeyError : continue
    
    def remove_page(self, page) :
        if page > 0 and page <= 300 :
            try :
                del self.notes[page]
            except KeyError :
                print("해당 페이지는 공백입니다.")

        else :
            print("페이지를 정확히 입력하여 주십시오.")
        # if page in self.notes.keys() : 도 사용 가능
            # return self.notes.pop(page)
        # else : print("해당 페이지에는 아무것도 삽입되지 않았습니다.")

    def read_page(self, page) :
        if page > 0 and page <= 300 :
            try :
                print(self.notes[page])
            except KeyError :
                print("해당 페이지에는 아무것도 삽입되지 않았습니다.")
        else :
            print("올바른 범위의 페이지를 입력하여주십시오. 페이지는 1부터 300까지 있습니다.")

    def __str__(self) : # 공책에 내용이 삽입된 모든 페이지를 열람할 수 있음
        result = ''
        for i in range(301) :
            try :
                result = result + "\n" + str(i) + ' : ' + str(self.notes[i])
            except KeyError : continue
        return result
#-*- coding: utf-8 -*-

class LxmlUtils():
    """ 
    we could not handle empty string between td tag if we use xpath './td/text()' 
    so we need to check each td.text one by one.
    """
    def get_text_list(self, tag_list):
        text_list = []
        for tag in tag_list:
            if tag.text is None:
                text_list.append('')
            else:
                text_list.append(tag.text)
        return text_list

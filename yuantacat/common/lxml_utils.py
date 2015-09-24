#-*- coding: utf-8 -*-

import lxml.html

class LxmlUtils():
    def get_text_list(self, tag_list):
        """Get text list for tag list

        Get text list for lxml tags.  We expect that text is negative number 
        literal if tag is enclosed by <p></p>.  We also expect that text is 
        empty string if text() is None.

        Args: 
            tag_list: A list of lxml tags

        Returns:
            A text list which length is equal to the length of tag_list
        """
        text_list = []
        for tag in tag_list:
            if tag.text is None:
                negative_number = tag.xpath('./p')
                if negative_number and negative_number[0].text:
                    text_list.append(negative_number[0].text)
                else:
                    text_list.append('')
            else:
                text_list.append(tag.text)
        return text_list

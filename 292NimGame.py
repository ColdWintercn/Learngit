#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 == 0 :
            return False
        else :
            return True
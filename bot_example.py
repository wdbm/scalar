#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
################################################################################
#                                                                              #
# bot_example                                                                  #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# The program is a scalar example bot.                                         #
#                                                                              #
# copyright (C) 2018 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for     #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################
"""

import logging

import megaparsex
import scalar
import technicolor

name        = "bot_example"
__version__ = "2018-08-23T1930Z"

log = logging.getLogger(name)
log.addHandler(technicolor.ColorisingStreamHandler())
log.setLevel(logging.DEBUG)
log.debug(name + " " + __version__)

def main():
    scalar.setup()
    scalar.room.send_text(name + " active")
    scalar.room.add_listener(on_message)
    scalar.client.start_listener_thread()
    while True:
        message = input()
        if message.lower() in ["exit", "quit"]:
            break
        else:
            scalar.room.send_text(message)

def on_message(room, event):
    log.debug("event: " + str(event))
    if event["type"] == "m.room.message" and scalar.config["username"] not in event["sender"]:
        if event["content"]["msgtype"] == "m.text":
            text = event["content"]["body"]
            log.info("{sender}: {message}".format(
                sender  = event["sender"],
                message = text
            ))
            if "status" in text.lower():
                scalar.room.send_text(megaparsex.report_system_status())
            elif "ip" in text.lower():
                scalar.room.send_text(megaparsex.report_IP())
            else:
                scalar.room.send_text("hello world")

if __name__ == "__main__":
    main()

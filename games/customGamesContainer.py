#-------------------------------------------------------------------------------
# Copyright (c) 2014 Gael Honorez.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Public License v3.0
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/gpl.html
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#-------------------------------------------------------------------------------

import time

from .gamesContainer import  gamesContainerClass
from games.customGame import customGame


class customGamesContainerClass(gamesContainerClass):
    '''Class for custom games'''

    def __init__(self, db, parent=None):
        super(customGamesContainerClass, self).__init__("faf", "Forged Alliance Forever" , db, parent)

    def addBasicGame(self, player, newgame, gamePort):
        playerLogin = player.getLogin()
        playerUuid = player.getId()
        playerState = player.action
        gameUuid = self.createUuid(playerUuid)

        if playerState == "PLAYING":
            return False
        elif playerState == "HOST":
            return False
        elif playerState == "JOIN":
            return False
        
        ngame = customGame(gameUuid, self)
        ngame.setLobbyState('Idle')
        ngame.setGameHostName(playerLogin)
        ngame.setGameHostUuid(playerUuid)
        ngame.setGameHostPort(gamePort)
        ngame.setGameHostLocalPort(gamePort)
        ngame.setGameName(newgame)
        self.games.append(ngame)
        return ngame

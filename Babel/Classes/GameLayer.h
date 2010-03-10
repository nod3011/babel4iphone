// This file is part of babel4iphone.

// Copyright (C) 2009 Giovanni Amati <amatig@gmail.com>

// babel4iphone is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.

// babel4iphone is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.

// You should have received a copy of the GNU General Public License
// along with babel4iphone.  If not, see <http://www.gnu.org/licenses/>.


#ifndef __GAME_LAYER_H__
#define __GAME_LAYER_H__

#ifndef COCOS2D_VERSION
#import "cocos2d.h"
#endif

#import "Character.h"
#import "InterfaceLayer.h"

@interface GameLayer : CCLayer
{

}

-(void) addMyCharacter:(NSArray *)baseInfo position:(int)p;
-(void) addEnemyCharacter:(NSArray *)baseInfo position:(int)p;
-(void) playFight;

@end

#endif

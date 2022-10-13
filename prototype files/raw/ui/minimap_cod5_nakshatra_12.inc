#define COMPASS_SIZE_SP		151
#define MINIMAP_X_SP        -855
#define MINIMAP_Y_SP        12
#define MINIMAP_W_SP        125
#define	MINIMAP_H_SP        125

#define MINIMAP_RECT 	0 0 COMPASS_SIZE_SP COMPASS_SIZE_SP HORIZONTAL_ALIGN_RIGHT VERTICAL_ALIGN_TOP
#define MINIMAP_ORIGIN  6 6

#define SO_VIS_MAP_DISPLAY					!dvarBool( ui_hidemap ) && \
											dvarstring( mapname ) != "airplane"
#define OBJECTIVES_TEXT_ACTIVE ( gamemsgwndactive( 0 ) )
						
// Minimap
menuDef
{
    name			"Compass_old"
    rect			MINIMAP_RECT
    fullScreen		0
    hiddenDuringScope
    hiddenDuringFlashbang
	visible when    (dvarInt("enable_minimap") == 1);

    // map --------------------
    itemDef
    {
        name			"minimapTickerBorder"
        rect			MINIMAP_X_SP (MINIMAP_Y_SP - 15) MINIMAP_W_SP 14
        origin 			MINIMAP_ORIGIN
        forecolor		1 1 1 1
        background		"minimap_tickertape_background"
        ownerdraw		CG_PLAYER_COMPASS_BACK
        visible         1
        decoration
    }
    itemDef
    {
        name			"minimapTicker"
        rect			MINIMAP_X_SP (MINIMAP_Y_SP - 12) MINIMAP_W_SP 9
        origin 			MINIMAP_ORIGIN
        forecolor		1 1 1 1
        background		"minimap_tickertape"
        ownerdraw		CG_PLAYER_COMPASS_TICKERTAPE_NO_OBJ
        textscale		0.25
		textstyle		ITEM_TEXTSTYLE_SHADOWED
        visible         1
        decoration
    }
    itemDef
    {
        name            "minimap"
        rect			MINIMAP_X_SP MINIMAP_Y_SP MINIMAP_W_SP MINIMAP_H_SP
        origin 			MINIMAP_ORIGIN
        forecolor		1 1 1 1
        background		"compass_map_default"
        ownerdraw		CG_PLAYER_COMPASS_MAP
        visible 		1
        decoration
    }

    // objectives --------------------
    itemDef
    {
        name			"compassplayer"
        rect			MINIMAP_X_SP MINIMAP_Y_SP MINIMAP_W_SP MINIMAP_H_SP
	 	origin 			MINIMAP_ORIGIN
        forecolor		1 1 1 1
        background		"compassping_player"
        ownerdraw		CG_PLAYER_COMPASS_PLAYER              // bugged
        visible 		1
        decoration
    }

    itemDef
    {
        rect			MINIMAP_X_SP MINIMAP_Y_SP MINIMAP_W_SP MINIMAP_H_SP
	 	origin 			MINIMAP_ORIGIN
        forecolor		1 1 1 1
        background		"objective_line"
        ownerdraw		CG_PLAYER_COMPASS_POINTERS
        visible 		1
        decoration
    }

    itemDef
    {
        name			"compassfriendlies"
        rect			MINIMAP_X_SP MINIMAP_Y_SP MINIMAP_W_SP MINIMAP_H_SP
	 	origin 			MINIMAP_ORIGIN
        forecolor		1 1 1 1
        background		"compassping_friendly"
        ownerdraw		CG_PLAYER_COMPASS_ACTORS
        visible 		1
        decoration
    }
	
    itemDef
    {
        name            "compasstanks"
		rect			MINIMAP_X_SP MINIMAP_Y_SP MINIMAP_W_SP MINIMAP_H_SP
	 	origin 			MINIMAP_ORIGIN
        forecolor		1 1 1 1
        background		"hud_objective_tank"
        ownerdraw		CG_PLAYER_COMPASS_TANKS
        visible 		1
        decoration
    }
	
	itemDef
    {
        name			"minimapBG"
        rect			(MINIMAP_X_SP - 16) (MINIMAP_Y_SP - 7) COMPASS_SIZE_SP COMPASS_SIZE_SP
        origin 			MINIMAP_ORIGIN
        forecolor		1 1 1 1
        background		"minimap_background"
        ownerdraw		CG_PLAYER_COMPASS_BACK
        visible         1
        decoration
    }
}

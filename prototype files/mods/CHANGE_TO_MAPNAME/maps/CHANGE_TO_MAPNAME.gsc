#include common_scripts\utility; 
#include maps\_utility;

main()
{
	//---|--|---\\
	// PRE LOAD
	//---|--|---\\
	
	maps\CHANGE_TO_MAPNAME_fx::main();
	
	include_weapons();
	include_powerups();
	
	//---|--|---\\
	// POST LOAD
	//---|--|---\\
	
	maps\_zombiemode::main();

	init_sounds();
}

include_weapons()


include_weapon( weapon_name )
{
	maps\_zombiemode_weapons::include_zombie_weapon( weapon_name );
}

include_powerups()
{
	include_powerup( "nuke" );
	include_powerup( "insta_kill" );
	include_powerup( "double_points" );
	include_powerup( "full_ammo" );
}

include_powerup( powerup_name )
{
	maps\_zombiemode_powerups::include_zombie_powerup( powerup_name );
}

init_sounds()
{
	maps\_zombiemode_utility::add_sound( "break_stone", "break_stone" );
}

#include maps\_utility; 
#include common_scripts\utility;

main()
{
	maps\createfx\CHANGE_TO_MAPNAME_fx::main();
	maps\createart\CHANGE_TO_MAPNAME_art::main();

	scriptedFX();
	precache_createfx_fx();
	footsteps(); 
}

scriptedFX()
{
}

// --- Ambient_Effects ---//
precache_createfx_fx()
{
	level._effect["fog_thick"] = loadfx("env/smoke/fx_fog_rolling_thick_600x600");
}

footsteps()
{
	animscripts\utility::setFootstepEffect( "asphalt",    LoadFx( "bio/player/fx_footstep_dust" ) );
	animscripts\utility::setFootstepEffect( "brick",      LoadFx( "bio/player/fx_footstep_dust" ) );
	animscripts\utility::setFootstepEffect( "carpet",     LoadFx( "bio/player/fx_footstep_dust" ) );
	animscripts\utility::setFootstepEffect( "cloth",      LoadFx( "bio/player/fx_footstep_dust" ) );
	animscripts\utility::setFootstepEffect( "concrete",   LoadFx( "bio/player/fx_footstep_dust" ) );
	animscripts\utility::setFootstepEffect( "dirt",       LoadFx( "bio/player/fx_footstep_sand" ) );
	animscripts\utility::setFootstepEffect( "foliage",    LoadFx( "bio/player/fx_footstep_dust" ) );
	animscripts\utility::setFootstepEffect( "gravel",     LoadFx( "bio/player/fx_footstep_sand" ) );
	animscripts\utility::setFootstepEffect( "grass",      LoadFx( "bio/player/fx_footstep_sand" ) );
	animscripts\utility::setFootstepEffect( "ice",        LoadFx( "bio/player/fx_footstep_snow" ) );
	animscripts\utility::setFootstepEffect( "metal",      LoadFx( "bio/player/fx_footstep_dust" ) );
	animscripts\utility::setFootstepEffect( "mud",        LoadFx( "bio/player/fx_footstep_mud" ) );
	animscripts\utility::setFootstepEffect( "paper",      LoadFx( "bio/player/fx_footstep_dust" ) );
	animscripts\utility::setFootstepEffect( "plaster",    LoadFx( "bio/player/fx_footstep_dust" ) );
	animscripts\utility::setFootstepEffect( "rock",       LoadFx( "bio/player/fx_footstep_sand" ) );
	animscripts\utility::setFootstepEffect( "sand",       LoadFx( "bio/player/fx_footstep_sand" ) );
	animscripts\utility::setFootstepEffect( "snow",       LoadFx( "bio/player/fx_footstep_snow" ) );
	animscripts\utility::setFootstepEffect( "water",      LoadFx( "bio/player/fx_footstep_water" ) );
	animscripts\utility::setFootstepEffect( "wood",       LoadFx( "bio/player/fx_footstep_dust" ) );
}

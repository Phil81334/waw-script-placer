#include clientscripts\_utility;

main()
{
	clientscripts\createfx\CHANGE_TO_MAPNAME_fx::main();

	footsteps();
	precache_createfx_fx();
	
	disableFX = GetDvarInt( "disable_fx" );
	if( !IsDefined( disableFX ) || disableFX <= 0 )
	{
		precache_scripted_fx();
	}
} 

precache_scripted_fx()
{
	level._effect["zombie_grain"]	= LoadFx( "misc/fx_zombie_grain_cloud" );
}

footsteps()
{
	clientscripts\_utility::setFootstepEffect( "asphalt",    LoadFx( "bio/player/fx_footstep_dust" ) );
	clientscripts\_utility::setFootstepEffect( "brick",      LoadFx( "bio/player/fx_footstep_dust" ) );
	clientscripts\_utility::setFootstepEffect( "carpet",     LoadFx( "bio/player/fx_footstep_dust" ) );
	clientscripts\_utility::setFootstepEffect( "cloth",      LoadFx( "bio/player/fx_footstep_dust" ) );
	clientscripts\_utility::setFootstepEffect( "concrete",   LoadFx( "bio/player/fx_footstep_dust" ) );
	clientscripts\_utility::setFootstepEffect( "dirt",       LoadFx( "bio/player/fx_footstep_sand" ) );
	clientscripts\_utility::setFootstepEffect( "foliage",    LoadFx( "bio/player/fx_footstep_dust" ) );
	clientscripts\_utility::setFootstepEffect( "gravel",     LoadFx( "bio/player/fx_footstep_sand" ) );
	clientscripts\_utility::setFootstepEffect( "grass",      LoadFx( "bio/player/fx_footstep_sand" ) );
	clientscripts\_utility::setFootstepEffect( "ice",        LoadFx( "bio/player/fx_footstep_snow" ) );
	clientscripts\_utility::setFootstepEffect( "metal",      LoadFx( "bio/player/fx_footstep_dust" ) );
	clientscripts\_utility::setFootstepEffect( "mud",        LoadFx( "bio/player/fx_footstep_mud" ) );
	clientscripts\_utility::setFootstepEffect( "paper",      LoadFx( "bio/player/fx_footstep_dust" ) );
	clientscripts\_utility::setFootstepEffect( "plaster",    LoadFx( "bio/player/fx_footstep_dust" ) );
	clientscripts\_utility::setFootstepEffect( "rock",       LoadFx( "bio/player/fx_footstep_sand" ) );
	clientscripts\_utility::setFootstepEffect( "sand",       LoadFx( "bio/player/fx_footstep_sand" ) );
	clientscripts\_utility::setFootstepEffect( "snow",       LoadFx( "bio/player/fx_footstep_snow" ) );
	clientscripts\_utility::setFootstepEffect( "water",      LoadFx( "bio/player/fx_footstep_water" ) );
	clientscripts\_utility::setFootstepEffect( "wood",       LoadFx( "bio/player/fx_footstep_dust" ) );
}

// --- Ambient_Effects ---//
precache_createfx_fx()
{
	level._effect["fog_thick"]			= loadfx("env/smoke/fx_fog_rolling_thick_600x600");
}

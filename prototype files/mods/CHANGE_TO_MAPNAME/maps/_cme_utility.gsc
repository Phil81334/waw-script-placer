#include common_scripts\utility; 
#include maps\_utility;

// <boolean to wait for flag_wait, function to pass players to, param1(else put undefined), param2(else put undefined), param3(else put undefined), boolean to thread or not>
pass_players(use_flag, func, param1, param2, param3, bool) {

	if ( use_flag )
		flag_wait( "all_players_connected" );
	
	players = get_players();
	
	for(i=0;i<=players.size;i++) {
	
		if ( isdefined( bool ) && bool ) {
		
			if( isdefined( param3 ) )
				players[i] thread [[ func ]]( param1, param2, param3 );
			else if( isdefined( param2 ) )
				players[i] thread [[ func ]]( param1, param2 );
			else if( isdefined( param1 ) )
				players[i] thread [[ func ]]( param1 );
			else
				players[i] thread [[ func ]]();
		}
		else {
		
			if( isdefined( param3 ) )
				players[i] [[ func ]]( param1, param2, param3 );
			else if( isdefined( param2 ) )
				players[i] [[ func ]]( param1, param2 );
			else if( isdefined( param1 ) )
				players[i] [[ func ]]( param1 );
			else
				players[i] [[ func ]]();
		}
	}
}

ternary(condition, on_true, on_false)
{
	// Developer script 1 has to be enabled for assertex to work
	
    // assertex( isDefined(condition), "Can't cast undefined to bool");
    // assertex( isDefined(on_true), "on true expression is not defined");
    // assertex( isDefined(on_false), "on false expression is not defined");
	
	// Problem with dev script 1 is that it can raise a stock code error. Aint nobody got time for this.
	// So i added the below.
	
	if ( !isDefined ( condition ) ) {
		iprintlnbold("ternary(condition): undefined");
		return undefined;
	}
	else if ( !isDefined ( on_true ) ) {
		iprintlnbold("ternary(on_true): undefined");
		return undefined;
	}
	else if ( !isDefined ( on_false ) ) {
		iprintlnbold("ternary(on_false): undefined");
		return undefined;
	}
	
    if(condition)
		return on_true;
	return on_false;
}
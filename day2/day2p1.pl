#!/usr/bin/perl -w
use List::Util qw[min max];

$total_cost = 0;

while ($line = <>){
	if ($line =~ /(\d+)x(\d+)x(\d+)/){
		$length = $1;
		$width = $2;
		$height = $3;
		$smallest_value = min($length*$width, $width*$height, $height*$length);
		$total_cost += 2*$length*$width + 2*$length*$height + 2*$height*$width;
		$total_cost += $smallest_value;
	}
}

print $total_cost, "\n";

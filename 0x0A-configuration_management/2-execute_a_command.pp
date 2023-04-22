# Using puppet to create a manifest that kill a process named killmenow.

exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => '/usr/bin/pgrep -f killmenow',
}


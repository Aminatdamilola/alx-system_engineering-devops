# create a file in /tmp using puppet.

file { '/tmp/school':
  content => "I love Puppet\n",
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}

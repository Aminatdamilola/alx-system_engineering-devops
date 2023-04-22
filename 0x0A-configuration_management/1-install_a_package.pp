# Using puppet to install flask from pip3.

exec { 'install flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => '/usr/local/bin:/usr/bin:/bin',
  creates => '/usr/local/lib/python3.6/dist-packages/flask',
}

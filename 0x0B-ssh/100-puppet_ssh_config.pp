#!/usr/bin/env bash
#apply puppet to configure ssh

file { '/home/ubuntu/.ssh/config':
  ensure => file,
  mode   => '0600',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  content => "
    Host 18.206.233.250
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}


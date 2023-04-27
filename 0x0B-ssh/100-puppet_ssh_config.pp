# apply puppet to set up your client SSH configuration file so that you can connect to a server without typing a password
include stdlib
file_line { 'Declaring identity file':
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}
file_line { 'turning off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true,
}

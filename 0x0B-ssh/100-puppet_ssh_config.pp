# configering ssh with puppet and also it good practise to do so
file_line { 'ssh_private_key':
  ensure  => present,
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^IdentityFile',
  path    => '/etc/ssh/ssh_config',
  replace => true,
}

file_line { 'disable_password_authentication':
  ensure  => present,
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication',
  path    => '/etc/ssh/sshd_config',
  replace => true,
}

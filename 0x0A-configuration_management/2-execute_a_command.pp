# create a manifest that kills a process named killmenow. using pupet
exec {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
  onlyif   => 'pgrep killmenow',
}

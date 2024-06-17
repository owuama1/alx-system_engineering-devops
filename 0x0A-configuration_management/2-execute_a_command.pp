# This Puppet manifest kills a process named killmenow using pkill.
exec { 'kill_killmenow_process':
  command     => '/usr/bin/pkill killmenow',
  path        => '/usr/bin:/usr/sbin:/bin:/sbin',
  refreshonly => true,
  subscribe   => Service['some_service'],
}

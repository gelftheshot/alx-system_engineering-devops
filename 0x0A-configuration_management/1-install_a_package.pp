#!/usr/bin/pup
# Install an especific version of flask using pupet master
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

Value INTERFACE_NAME (\S+)
Value LINE_STATUS ((up|down))
Value ADMIN_STATE ((up|down))
Value MAC_ADDR ([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})
Value MTU (\d+)
Value DUPLEX (\S+)
Value SPEED (\d+)


Start
  ^${INTERFACE_NAME} is ${LINE_STATUS}$$ 
  ^admin state is ${ADMIN_STATE},
  ^  Hardware.*address:\s+${MAC_ADDR}\s
  ^  MTU ${MTU} bytes 
  ^  ${DUPLEX}-duplex, ${SPEED} Mb/s -> Record 

EOF

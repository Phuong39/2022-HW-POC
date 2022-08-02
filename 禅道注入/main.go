package main

import (
	"flag"
	"fmt"
	"github.com/gookit/color"
)

func main() {
	var host, file string

	zentao := &Zentao{}

	flag.StringVar(&host, "h", "", "ip")
	flag.StringVar(&file, "f", "", "filepath")
	flag.Parse()

	view := `
  ___  _  _  _  _  ____        ___    ___   ___   ___         __   ___   ___  ___  ___ 
 / __)( \( )( \/ )(  _ \  ___ (__ \  / _ \ (__ \ (__ \  ___  /. | (__ \ ( _ )| __)(__ )
( (__  )  (  \  /  )(_) )(___) / _/ ( (_) ) / _/  / _/ (___)(_  _) / _/ / _ \|__ \ (_ \
 \___)(_)\_)  \/  (____/      (____) \___/ (____)(____)       (_) (____)\___/(___/(___/  by:Z92G`
	color.Cyan.Println(view)
	fmt.Println()

	if file != "" && host == "" {
		zentao.batchScan(file)
	} else {
		zentao.singleScan(host)
	}
}

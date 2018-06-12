import time
import sys



def progress_tracker(current_value, highest_value, initial_time):
    """ Provide a progress tracker to keep value updated until finishes """
    if (current_value is None or
         highest_value is None or
          highest_value == 0 or
           initial_time is None):
        return

    try:
        real_time = time.time()
        progress_percent = int((current_value/highest_value)*100)
        
        elapsed_time = real_time-initial_time
        elapsed_formatted = float("{0:.2f}".format(elapsed_time))
        elapsed = ("{} seconds".format(elapsed_formatted) if elapsed_formatted < 60 else
               "{} minutes".format(float("{0:.2f}".format(elapsed_formatted/60))))

        eta_time = abs((elapsed_time*100)/(progress_percent if progress_percent != 0 else 1)-elapsed_time)
        eta_formatted = float("{0:.2f}".format(eta_time))
        eta = ("{} seconds".format(eta_formatted) if eta_formatted < 60 else
               "{} minutes".format(float("{0:.2f}".format(eta_formatted/60))))

        tracker_line = "-----------------------------------"
        filled_index = int(progress_percent/2.77)
        progress_container = "["+tracker_line[:filled_index]+"+"+tracker_line[filled_index:]+"]"
        progress_container = progress_container[:filled_index+1].replace("-", "=")+progress_container[filled_index+1:]

        total_message = ("\r  {}/{} {}  {}%    "
                            "|> Elapsed: {}    "
                                "|> ETA: {}      ".format(
                        current_value, highest_value, progress_container, progress_percent, elapsed, eta))

        sys.stdout.write(total_message)
        sys.stdout.flush()

    except:
        raise



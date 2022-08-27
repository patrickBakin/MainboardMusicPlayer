import pretty_midi

midi_data = pretty_midi.PrettyMIDI('FireFlies.mid')
filename= "FireFlies.ini"

PureRightHandNotes=[]
PureRightHandDuration=[]
PureRightHandStart=[]
PureRightHandStop=[]

PureLeftHandNotes=[]
PureLeftHandDuration=[]
PureLeftHandStart=[]
PureLeftHandStop=[]
for instrument in midi_data.instruments:
    for noteindex in range(len(instrument.notes)):
        if noteindex > 0 and (instrument.notes[noteindex].start == instrument.notes[noteindex-1].start):
            
            PureLeftHandNotes.append(
                f'{pretty_midi.note_number_to_hz(instrument.notes[noteindex].pitch)}')
            PureLeftHandDuration.append(f'{instrument.notes[noteindex].end - instrument.notes[noteindex].start}')
            PureLeftHandStart.append(f'{instrument.notes[noteindex].start}')
            PureLeftHandStop.append(f'{instrument.notes[noteindex].end}')
            continue
        if noteindex < len(instrument.notes)-1 and (instrument.notes[noteindex].start == instrument.notes[noteindex+1].start):
         

            PureRightHandNotes.append(
                f'{pretty_midi.note_number_to_hz(instrument.notes[noteindex].pitch)}')
            PureRightHandDuration.append(f'{instrument.notes[noteindex].end - instrument.notes[noteindex].start}')
            PureRightHandStart.append(f'{instrument.notes[noteindex].start}')
            PureRightHandStop.append(f'{instrument.notes[noteindex].end}')
            PureRightHandNotes.append(f'{pretty_midi.note_number_to_hz( instrument.notes[noteindex].pitch)}')
            #PureRightHandDuration.append(f'{instrument.notes[noteindex].end-instrument.notes[noteindex].start}')
            continue
        if instrument.notes[noteindex].pitch>=70:
          

            PureRightHandNotes.append(
                    f'{pretty_midi.note_number_to_hz(instrument.notes[noteindex].pitch)}')
            PureRightHandDuration.append(f'{instrument.notes[noteindex].end - instrument.notes[noteindex].start}')
            PureRightHandStart.append(f'{instrument.notes[noteindex].start}')
            PureRightHandStop.append(f'{instrument.notes[noteindex].end}')
            continue
        if instrument.notes[noteindex].pitch<70:
           
            PureLeftHandNotes.append(
                f'{pretty_midi.note_number_to_hz(instrument.notes[noteindex].pitch)}')
            PureLeftHandDuration.append(f'{instrument.notes[noteindex].end - instrument.notes[noteindex].start}')
            PureLeftHandStart.append(f'{instrument.notes[noteindex].start}')
            PureLeftHandStop.append(f'{instrument.notes[noteindex].end}')
          
            continue
      




textfile = open(filename,"w")

textfile.write("NotesR=")
for element in PureRightHandNotes:

    textfile.write(element+",")



textfile.write("\nDurationR=")
for element in PureRightHandDuration:

    textfile.write(element+",")

textfile.write("\nStartR=")
for element in PureRightHandStart:

    textfile.write(element+",")

textfile.write("\nStopR=")
for element in PureRightHandStop:

    textfile.write(element+",")






textfile.write("\nNotesL=")
for element in PureLeftHandNotes:

    textfile.write(element+",")



textfile.write("\nDurationL=")
for element in PureLeftHandDuration:

    textfile.write(element+",")

textfile.write("\nStartL=")
for element in PureLeftHandStart:

    textfile.write(element+",")

textfile.write("\nStopL=")
for element in PureLeftHandStop:

    textfile.write(element+",")






textfile.close()



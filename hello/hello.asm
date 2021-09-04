; vasm6502_oldstyle intro.asm -Fbin -cbm-prg
	org $0801
	db $0E, $08,$0A,$00,$9E,$20,$28,$32,$30,$36,$34,$29,$00,$00,$00

	lda #$0E
	jsr	$ffd2

	lda #>HelloWorld
	sta $21
	lda #<HelloWorld
	sta $20

	jsr PrintStr
	rts

PrintStr:
	ldy #0
PrintStr_again:
	lda	($20),y
	cmp #255 ; $FF?
	beq PrintStr_Done
	jsr	PrintChar
	iny
	jmp PrintStr_again ;loop
PrintStr_Done:
	rts
PrintChar:
	cmp #64
	bcc PrintCharOKB
	eor #%00100000
PrintCharOKB:
	jmp $FFD2
HelloWorld:
	db "Hello World"
	db 255
